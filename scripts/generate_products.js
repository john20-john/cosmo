#!/usr/bin/env node
// scripts/generate_products.js
// Usage: node scripts/generate_products.js [count] [outputPath]
// Example: node scripts/generate_products.js 100000 products.generated.json

const fs = require('fs');
const path = require('path');

const count = Number(process.argv[2]) || 100000;
const outPath = process.argv[3] || path.join(process.cwd(), 'products.generated.json');

function randPrice() {
  return Number((Math.random() * 200).toFixed(2));
}

const arabicNames = ['كريم','زيت','شامبو','بلسم','لوشن','ماسك','مزيل عرق','صابون','معجون أسنان','مستحضر'];
const imgPlaceholder = (i) => `https://picsum.photos/seed/${i}/500/500`;

const products = [];
const baseId = Date.now();
for (let i = 1; i <= count; i++) {
  const id = baseId * 1000 + i;
  const name = `منتج تجريبي ${i} ${arabicNames[i % arabicNames.length]}`;
  products.push({ id, name, price: randPrice(), image: imgPlaceholder(i) });
  if (i % 10000 === 0) process.stdout.write(`generated ${i}\n`);
}

fs.writeFileSync(outPath, JSON.stringify(products, null, 2));
console.log(`wrote ${count} products to ${outPath}`);
