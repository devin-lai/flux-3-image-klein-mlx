// Asset-only developer tool: npm install --no-save sharp; node scripts/render_assets.cjs
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '..');
(async () => {
  await sharp(fs.readFileSync(path.join(root, 'docs/assets/social-preview.svg')))
    .png({palette: true, quality: 100}).toFile(path.join(root, 'docs/assets/social-preview.png'));
})();
