#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const filtered = args.filter(num => num !== max);
  const secondMax = Math.max(...filtered);
  console.log(secondMax);
}
