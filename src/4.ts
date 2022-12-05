import assert from "assert"
import { input } from "./util.js"

class Range {
  constructor(public start: number, public end: number) {}

  static parse(input: string) {
    const [start, end] = input.split("-").map((d) => parseInt(d))
    return new Range(start, end)
  }

  contains(other: Range): boolean {
    return this.start <= other.start && this.end >= other.end
  }

  overlaps(other: Range) {
    return this.start <= other.end && this.end >= other.start
  }
}

function parseInput(input: string) {
  return input.split("\n").map((line): [Range, Range] => {
    const [first, second] = line.split(",")
    return [Range.parse(first), Range.parse(second)]
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
