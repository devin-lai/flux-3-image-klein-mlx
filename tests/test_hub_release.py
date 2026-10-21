"""Checks for accidental multi-variant downloads and optional-dependency regressions."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

from flux_klein_mlx.hub import download_variant

ROOT = Path(__file__).resolve().parents[1]


class DownloadTests(unittest.TestCase):
    def test_every_variant_selects_only_its_own_repository(self):
        calls = []
        fake = types.ModuleType('huggingface_hub')
        fake.snapshot_download = lambda **kwargs: calls.append(kwargs) or str(kwargs['local_dir'])
        with tempfile.TemporaryDirectory() as scratch, patch.dict(sys.modules, {'huggingface_hub': fake}):
            for variant in ('q8-quality', 'q8', 'mixed', 'q4', 'bf16'):
                destination = Path(scratch) / variant
                self.assertEqual(download_variant(variant, destination, revision='abc123'), destination.resolve())
                self.assertEqual(calls[-1]['repo_id'], f'devin-lai/flux-3-image-klein-mlx-{variant}')
                self.assertEqual(calls[-1]['revision'], 'abc123')
        self.assertEqual(len(calls), 5)

    def test_existing_different_variant_is_rejected_before_network_use(self):
        with tempfile.TemporaryDirectory() as scratch:
            (Path(scratch) / 'model_index.json').write_text(json.dumps({'variants': {'q4': {}}}))
            with self.assertRaisesRegex(ValueError, 'separate model directory'):
                download_variant('q8-quality', scratch)

    def test_missing_hub_dependency_has_a_direct_install_command(self):
        with tempfile.TemporaryDirectory() as scratch, patch.dict(sys.modules, {'huggingface_hub': None}):
            with self.assertRaisesRegex(RuntimeError, 'pip install "huggingface_hub>=1,<3"'):
                download_variant('q4', scratch)

    def test_unknown_variant_and_runtime_destination_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            download_variant('../unrelated-repo', '/tmp/unused-flux-test')
        with self.assertRaisesRegex(ValueError, 'outside'):
            download_variant('q4', ROOT / 'weights')

    def test_download_only_does_not_import_mlx_or_require_model_metadata(self):
        from flux_klein_mlx.__main__ import main
        with tempfile.TemporaryDirectory() as scratch:
            args = ['flux-klein', '--download', 'q4', '--download-only', '--model-dir', scratch]
            with patch.object(sys, 'argv', args), patch('flux_klein_mlx.hub.download_variant') as download:
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    main()
                self.assertIn('Downloaded q4', output.getvalue())
                download.assert_called_once_with('q4', Path(scratch).resolve(), revision=None)
        self.assertNotIn('mlx.core', sys.modules)


class CommandTests(unittest.TestCase):
    def test_standalone_package_lists_only_available_presets_without_mlx(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / 'model_index.json').write_text(json.dumps({
                'default_variant': 'q4', 'variants': {'q4': {
                    'transformer': 'q4', 'text_encoder': 'q8', 'download_bytes': 1024,
                }},
            }))
            (root / 'presets.json').write_text(json.dumps({'presets': {
                'q4-16': {'variant': 'q4', 'steps': 16},
                'q8-quality-16': {'variant': 'q8-quality', 'steps': 16},
            }}))
            result = subprocess.run([sys.executable, '-m', 'flux_klein_mlx', '--model-dir', scratch, '--list'],
                                    cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('q4-16', result.stdout)
            self.assertNotIn('q8-quality', result.stdout)

    def test_revision_without_download_cannot_silently_run_another_model(self):
        result = subprocess.run([sys.executable, '-m', 'flux_klein_mlx', '--revision', 'abc123'],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('require --download', result.stderr)


if __name__ == '__main__':
    unittest.main()
