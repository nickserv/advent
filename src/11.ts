import assert from "assert/strict";
import { input } from "./util.js";

function product(numbers: number[]) {
	return numbers.reduce((a, b) => a * b);
}

class Monkey {
	inspected = 0;

	constructor(
		private items: number[],
		private operation: "+" | "*",
		private operand: number | undefined,
		public divisor: number,
		private divisible: number,
		private indivisible: number,
	) {}

	static parse(input: string) {
		return Array.from(
			input.matchAll(
				/Monkey \d:\n  Starting items: ([\d, ]+)\n  Operation: new = old (.) (old|\d+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d)\n    If false: throw to monkey (\d)/g,
			),
			([, items, operation, operand, divisor, divisible, indivisible]) =>
				new Monkey(
					items.split(", ").map((item) => parseInt(item)),
					operation as Monkey["operation"],
					operand !== "old" ? parseInt(operand) : undefined,
					parseInt(divisor),
					parseInt(divisible),
					parseInt(indivisible),
				),
		);
	}

	inspect(monkeys: Monkey[], worry = false) {
		for (let item of this.items) {
			switch (this.operation) {
				case "+":
					item += this.operand ?? item;
					break;
				case "*":
					item *= this.operand ?? item;
					break;
			}

			if (worry) item %= product(monkeys.map((monkey) => monkey.divisor));
			else item = Math.floor(item / 3);

			const target = !(item % this.divisor) ? this.divisible : this.indivisible;
			monkeys[target].items.push(item);
			this.inspected++;
		}
		this.items = [];
	}
}

function inspectAll(monkeys: Monkey[], rounds: number, worry = false) {
	for (let i = 0; i < rounds; i++) {
		for (const monkey of monkeys) {
			monkey.inspect(monkeys, worry);
		}
	}
}

function monkeyBusiness(monkeys: Monkey[]) {
	const [first, second] = monkeys
		.map((monkey) => monkey.inspected)
		.sort((a, b) => b - a);
	return first * second;
}

const testInput = `Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1`;
let testMonkeys = Monkey.parse(testInput);
inspectAll(testMonkeys, 20);
assert.equal(monkeyBusiness(testMonkeys), 10_605);

let monkeys = Monkey.parse(await input(11));
inspectAll(monkeys, 20);
console.log(monkeyBusiness(monkeys));

testMonkeys = Monkey.parse(testInput);
inspectAll(testMonkeys, 10_000, true);
assert.equal(monkeyBusiness(testMonkeys), 2_713_310_158);

monkeys = Monkey.parse(await input(11));
inspectAll(monkeys, 10_000, true);
console.log(monkeyBusiness(monkeys));
