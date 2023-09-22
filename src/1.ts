import { input, sum } from "./util.js";

const calories = (await input(1))
	.split("\n\n")
	.map((section) => section.split("\n").map((line) => parseInt(line)));
const totalCalories = calories.map(sum);

console.log(Math.max(...totalCalories));
console.log(sum(totalCalories.sort((a, b) => b - a).slice(0, 3)));
