#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: node 102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const sourceFile1 = args[0];
const sourceFile2 = args[1];
const destinationFile = args[2];

try {
  const data1 = fs.readFileSync(sourceFile1, 'utf8');
  const data2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenatedData = `${data1}${data2}`;

  fs.writeFileSync(destinationFile, concatenatedData);

  console.log(`Concatenated data has been written to ${destinationFile}`);
} catch (err) {
  console.error('Error:', err.message);
}
