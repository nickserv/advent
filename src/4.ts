import assert from "assert"
import { input } from "./util.js"

interface Range {
  start: number
  end: number
}

function parseInput(input: string) {
  return input.split("\n").map((line): [Range, Range] => {
    const numbers = /(\d+)-(\d+),(\d+)-(\d+)/
      .exec(line)!
      .slice(1)
      .map((d) => parseInt(d))
    return [
      { start: numbers[0], end: numbers[1] },
      { start: numbers[2], end: numbers[3] },
    ]
  })
}

function count<T>(array: T[], predicate: (value: T) => boolean) {
  return array.filter(predicate).length
}

function rangeContains(range1: Range, range2: Range) {
  return range1.start <= range2.start && range1.end >= range2.end
}

function containedRanges(ranges: [Range, Range][]) {
  return count(
    ranges,
    ([range1, range2]) =>
      rangeContains(range1, range2) || rangeContains(range2, range1),
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

function rangeOverlaps(range1: Range, range2: Range) {
  return range1.start <= range2.end && range1.end >= range2.start
}

function overlappingRanges(ranges: [Range, Range][]) {
  return count(ranges, ([range1, range2]) => rangeOverlaps(range1, range2))
}

assert.strictEqual(overlappingRanges(testRangePairs), 4)

console.log(overlappingRanges(rangePairs))
