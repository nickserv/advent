import assert from "assert"
import { input } from "./util.js"

function findMarker(input: string, length: number) {
  return [...input]
    .map((_, index) => index + length)
    .find((end, start) => new Set([...input.slice(start, end)]).size === length)
}

const testInputs = [
  "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
  "bvwbjplbgvbhsrlpgdmjqwftvncz",
  "nppdvjthqldpwncqszvftbrmjlhg",
  "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
  "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]
assert.strictEqual(findMarker(testInputs[0], 4), 7)
assert.strictEqual(findMarker(testInputs[1], 4), 5)
assert.strictEqual(findMarker(testInputs[2], 4), 6)
assert.strictEqual(findMarker(testInputs[3], 4), 10)
assert.strictEqual(findMarker(testInputs[4], 4), 11)
assert.strictEqual(findMarker(testInputs[0], 14), 19)
assert.strictEqual(findMarker(testInputs[1], 14), 23)
assert.strictEqual(findMarker(testInputs[2], 14), 23)
assert.strictEqual(findMarker(testInputs[3], 14), 29)
assert.strictEqual(findMarker(testInputs[4], 14), 26)

console.log(findMarker(await input(6), 4))
console.log(findMarker(await input(6), 14))
