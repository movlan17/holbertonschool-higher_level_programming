#!/usr/bin/node

// Bütün arqumentləri götür və nömrəyə çevir
const args = process.argv.slice(2).map(Number);

// Əgər arqument sayı 0 və ya 1-dirsə, ikinci ən böyük yoxdur
if (args.length < 2) {
  console.log(0);
} else {
  // Ən böyük ədədi tap
  const max = Math.max(...args);
  // Ən böyük ədədi çıxart və qalanlardan ikinci ən böyüyü tap
  const filtered = args.filter(num => num !== max);
  const secondMax = Math.max(...filtered);
  console.log(secondMax);
}
