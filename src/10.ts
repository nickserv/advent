import assert from "assert"
import { input, sum } from "./util.js"

function parseInstruction(input: string) {
  if (input.startsWith("addx ")) return parseInt(input.slice(5))
}

const testInstructions = `noop
addx 3
addx -5`
  .split("\n")
  .map(parseInstruction)
assert.deepStrictEqual(testInstructions, [undefined, 3, -5])

function execute(instructions: (number | undefined)[], x = 1): number[] {
  if (instructions.length) {
    const [instruction, ...rest] = instructions
    const next = instruction
      ? [x + instruction, ...execute(rest, x + instruction)]
      : execute(rest, x)
    return [x, ...next]
  } else return []
}

assert.deepStrictEqual(execute(testInstructions), [1, 1, 4, 4, -1])

const xs = execute((await input(10)).split("\n").map(parseInstruction))

const cycles = [20, 60, 100, 140, 180, 220]
function sumSignalStrengths(xs: number[]) {
  return sum(cycles.map((cycle) => cycle * xs[cycle - 2]))
}

const testXs = execute(
  `addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop`
    .split("\n")
    .map(parseInstruction),
)
assert.strictEqual(sumSignalStrengths(testXs), 13_140)

console.log(sumSignalStrengths(xs))

function render(xs: number[]) {
  let previous = 1
  return xs
    .map((next, index) => {
      const remainder = index % 40
      const newline = index && !remainder ? "\n" : ""
      const pixel = Math.abs(previous - remainder) < 2 ? "#" : "."
      previous = next
      return `${newline}${pixel}`
    })
    .join("")
}

assert.strictEqual(
  render(testXs),
  `##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....`,
)

console.log(render(xs))
