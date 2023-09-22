import assert from "assert/strict";
import { input } from "./util.js";

class Range {
	constructor(
		public start: number,
		public end: number,
	) {}

	static parse(input: string) {
		const [start, end] = input.split("-").map((d) => parseInt(d));
		return new Range(start, end);
	}

	contains(other: Range) {
		return this.start <= other.start && this.end >= other.end;
	}

	overlaps(other: Range) {
		return this.start <= other.end && this.end >= other.start;
	}
}

class RangePair {
	constructor(
		public first: Range,
		public second: Range,
	) {}

	static parse(input: string) {
		const [first, second] = input.split(",").map(Range.parse);
		return new RangePair(first, second);
	}

	contains() {
		return this.first.contains(this.second) || this.second.contains(this.first);
	}

	overlaps() {
		return this.first.overlaps(this.second);
	}
}

function parseInput(input: string) {
	return input.split("\n").map(RangePair.parse);
}

function count<T>(array: T[], predicate: (value: T) => boolean) {
	return array.filter(predicate).length;
}

function containedRanges(pairs: RangePair[]) {
	return count(pairs, (pair) => pair.contains());
}

const testRangePairs = parseInput(
	`2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`,
);
assert.equal(containedRanges(testRangePairs), 2);

const rangePairs = parseInput(await input(4));
console.log(containedRanges(rangePairs));

function overlappingRanges(pairs: RangePair[]) {
	return count(pairs, (pair) => pair.overlaps());
}

assert.equal(overlappingRanges(testRangePairs), 4);

console.log(overlappingRanges(rangePairs));
