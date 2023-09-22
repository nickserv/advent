import assert from "assert/strict";
import { input, sum } from "./util.js";

function parseSplitRucksack(line: string) {
	const pivot = line.length / 2;
	return [new Set(line.slice(0, pivot)), new Set(line.slice(pivot))];
}

function rucksackIntersection(rucksacks: Set<string>[]) {
	return [
		...rucksacks.reduce(
			(intersection, rucksack) =>
				new Set([...intersection].filter((char) => rucksack.has(char))),
		),
	][0];
}

const testLines = [
	"vJrwpWtwJgWrhcsFMMfFFhFp",
	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
	"PmmdzqPrVvPwwTWBwg",
	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
	"ttgJtRGJQctTZtZT",
	"CrZsJsPPZsGzwwsLwLmpwMDw",
];
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[0])), "p");
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[1])), "L");
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[2])), "P");
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[3])), "v");
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[4])), "t");
assert.equal(rucksackIntersection(parseSplitRucksack(testLines[5])), "s");

function priority(char: string) {
	return (
		char.charCodeAt(0) +
		(char === char.toUpperCase()
			? 27 - "A".charCodeAt(0)
			: 1 - "a".charCodeAt(0))
	);
}

assert.equal(priority("p"), 16);
assert.equal(priority("L"), 38);
assert.equal(priority("P"), 42);
assert.equal(priority("v"), 22);
assert.equal(priority("t"), 20);
assert.equal(priority("s"), 19);
assert.equal(
	sum(
		testLines.map((line) =>
			priority(rucksackIntersection(parseSplitRucksack(line))),
		),
	),
	157,
);

const lines = (await input(3)).split("\n");

console.log(
	sum(
		lines.map((line) =>
			priority(rucksackIntersection(parseSplitRucksack(line))),
		),
	),
);

assert.equal(
	rucksackIntersection(testLines.slice(0, 3).map((line) => new Set(line))),
	"r",
);
assert.equal(
	rucksackIntersection(testLines.slice(3).map((line) => new Set(line))),
	"Z",
);

function partition<T>(array: T[], n: number): T[][] {
	return array.length
		? [array.slice(0, n), ...partition(array.slice(n), n)]
		: [];
}

assert.equal(
	sum(
		partition(
			testLines.map((line) => new Set(line)),
			3,
		).map((rucksacks) => priority(rucksackIntersection(rucksacks))),
	),
	70,
);

console.log(
	sum(
		partition(
			lines.map((line) => new Set(line)),
			3,
		).map((rucksacks) => priority(rucksackIntersection(rucksacks))),
	),
);
