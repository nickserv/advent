import assert from "assert"
import { input } from "./util.js"

class Range {
  constructor(public start: number, public end: number) {}

  contains(other: Range): boolean {
    return this.start <= other.start && this.end >= other.end
  }

  overlaps(other: Range) {
    return this.start <= other.end && this.end >= other.start
  }
}

function parseInput(input: string): [Range, Range][] {
  return input.split("\n").map((string) => {
    const numbers = /(\d+)-(\d+),(\d+)-(\d+)/
      .exec(string)!
      .slice(1)
      .map((d) => parseInt(d))
    return [
      new Range(numbers[0], numbers[1]),
      new Range(numbers[2], numbers[3]),
    ]
  })
}

function count<T>(array: T[], predicate: (value: T) => boolean) {
  return array.filter(predicate).length
}

function containedRanges(ranges: [Range, Range][]) {
  return count(
    ranges,
    ([range1, range2]) => range1.contains(range2) || range2.contains(range1),
  )
}

const testRangePairs = parseInput(
  `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`,
)
assert.strictEqual(containedRanges(testRangePairs), 2)

const rangePairs = parseInput(await input(4))
console.log(containedRanges(rangePairs))

function overlappingRanges(ranges: [Range, Range][]) {
  return count(ranges, ([range1, range2]) => range1.overlaps(range2))
}

assert.strictEqual(overlappingRanges(testRangePairs), 4)

console.log(overlappingRanges(rangePairs))
