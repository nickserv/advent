import { readFile } from "fs/promises"

function sum(numbers: number[]) {
  return numbers.reduce((a, b) => a + b)
}

const calories = (await readFile("resources/1.txt", "utf8"))
  .trim()
  .split("\n\n")
  .map((section) => section.split("\n").map((line) => parseInt(line)))
const totalCalories = calories.map(sum)

console.log(Math.max(...totalCalories))
console.log(sum(totalCalories.sort((a, b) => b - a).slice(0, 3)))
