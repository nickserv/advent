import { input } from "./util.js"

function sum(numbers: number[]) {
  return numbers.reduce((a, b) => a + b)
}

const calories = (await input(1))
  .split("\n\n")
  .map((section) => section.split("\n").map((line) => parseInt(line)))
const totalCalories = calories.map(sum)

console.log(Math.max(...totalCalories))
console.log(sum(totalCalories.sort((a, b) => b - a).slice(0, 3)))
