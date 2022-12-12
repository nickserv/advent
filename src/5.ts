import assert from "assert/strict"
import { input } from "./util.js"

function parseStacks(input: string) {
  const lines: string[] = input.split("\n").slice(0, -1)
  return Array.from({ length: (lines[0].length - 3) / 4 + 1 }, (_, index) =>
    lines
      .map((line) => line[index * 4 + 1])
      .filter((char) => char !== " ")
      .reverse()
      .join(""),
  )
}

interface Move {
  quantity: number
  start: number
  end: number
}

function parseMove(line: string): Move {
  const [, quantity, start, end] = /move (\d+) from (\d+) to (\d+)/
    .exec(line)!
    .map((number) => parseInt(number))
  return { quantity, start, end }
}

function parseInput(input: string): [string[], Move[]] {
  const [stacksInput, movesInput] = input.split("\n\n")
  return [parseStacks(stacksInput), movesInput.split("\n").map(parseMove)]
}

const [testStacks, testMoves] = parseInput(`    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`)
assert.deepEqual(testStacks, ["ZN", "MCD", "P"])
assert.deepEqual(testMoves, [
  { quantity: 1, start: 2, end: 1 },
  { quantity: 3, start: 1, end: 3 },
  { quantity: 2, start: 2, end: 1 },
  { quantity: 1, start: 1, end: 2 },
])

function doMove(
  stacks: string[],
  { quantity, start, end }: Move,
  multiple = false,
): string[] {
  if (quantity) {
    const pivot = -(multiple ? quantity : 1)
    const movedStacks = stacks.map((stack, index) => {
      switch (index) {
        case start - 1:
          return stack.slice(0, pivot)
        case end - 1:
          return stack + stacks[start - 1].slice(pivot)
        default:
          return stack
      }
    })

    if (multiple) return movedStacks
    else return doMove(movedStacks, { quantity: quantity - 1, start, end })
  } else return stacks
}

function doMoves(stacks: string[], moves: Move[], multiple = false) {
  return moves.reduce((stacks, move) => doMove(stacks, move, multiple), stacks)
}

assert.deepEqual(doMoves(testStacks, testMoves), ["C", "M", "PDNZ"])
assert.deepEqual(doMoves(testStacks, testMoves, true), ["M", "C", "PZND"])

function message(stacks: string[]) {
  return stacks.map((stack) => stack.slice(-1)).join("")
}

assert.equal(message(["C", "M", "PDNZ"]), "CMZ")
assert.equal(message(["M", "C", "PZND"]), "MCD")

const [stacks, moves] = parseInput(await input(5))
console.log(message(doMoves(stacks, moves)))
console.log(message(doMoves(stacks, moves, true)))
