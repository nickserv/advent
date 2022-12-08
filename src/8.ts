import assert from "assert"
import { input } from "./util.js"

type Forest = number[][]

const Forest = {
  parse(input: string): Forest {
    return input
      .split("\n")
      .map((row) => row.split("").map((string) => parseInt(string)))
  },
}

enum Direction {
  Up,
  Down,
  Left,
  Right,
}

const directions = [
  Direction.Up,
  Direction.Down,
  Direction.Left,
  Direction.Right,
]

class Position {
  constructor(public row: number, public col: number) {}

  adjust(direction: Direction): Position {
    switch (direction) {
      case Direction.Up:
        return new Position(this.row - 1, this.col)
      case Direction.Down:
        return new Position(this.row + 1, this.col)
      case Direction.Left:
        return new Position(this.row, this.col - 1)
      case Direction.Right:
        return new Position(this.row, this.col + 1)
    }
  }
}

function findTreesInDirection(
  forest: Forest,
  position: Position,
  direction: Direction,
) {
  function inner(
    forest: Forest,
    position: Position,
    direction: Direction,
  ): number[] {
    const { row, col } = position
    if (
      row >= 0 &&
      row < forest.length &&
      col >= 0 &&
      col < forest[row].length
    ) {
      return [
        forest[row][col],
        ...inner(forest, position.adjust(direction), direction),
      ]
    } else {
      return []
    }
  }

  return inner(forest, position, direction).slice(1)
}

const testForest = Forest.parse(`30373
25512
65332
33549
35390`)
const middle = new Position(2, 2)
assert.deepStrictEqual(
  findTreesInDirection(testForest, middle, Direction.Up),
  [5, 3],
)
assert.deepStrictEqual(
  findTreesInDirection(testForest, middle, Direction.Down),
  [5, 3],
)
assert.deepStrictEqual(
  findTreesInDirection(testForest, middle, Direction.Left),
  [5, 6],
)
assert.deepStrictEqual(
  findTreesInDirection(testForest, middle, Direction.Right),
  [3, 2],
)

function isVisible(forest: Forest, position: Position) {
  const { row, col } = position
  const candidate = forest[row][col]
  return directions.some((direction) =>
    findTreesInDirection(forest, position, direction).every(
      (tree) => tree < candidate,
    ),
  )
}

for (const i of [0, 1, 2, 3, 4]) {
  assert(isVisible(testForest, new Position(0, i)))
  assert(isVisible(testForest, new Position(4, i)))
  assert(isVisible(testForest, new Position(i, 0)))
  assert(isVisible(testForest, new Position(i, 4)))
}

assert(isVisible(testForest, new Position(1, 1)))
assert(isVisible(testForest, new Position(1, 2)))
assert(!isVisible(testForest, new Position(1, 3)))
assert(isVisible(testForest, new Position(2, 1)))
assert(!isVisible(testForest, new Position(2, 2)))
assert(isVisible(testForest, new Position(2, 3)))
assert(!isVisible(testForest, new Position(3, 1)))
assert(isVisible(testForest, new Position(3, 2)))
assert(!isVisible(testForest, new Position(3, 3)))

function visibleCount(forest: Forest) {
  let count = 0
  for (let row = 0; row < forest.length; row++) {
    for (let col = 0; col < forest[row].length; col++) {
      if (isVisible(forest, new Position(row, col))) count++
    }
  }
  return count
}

assert.strictEqual(visibleCount(testForest), 21)

console.log(visibleCount(Forest.parse(await input(8))))

function distance(forest: Forest, position: Position, direction: Direction) {
  const { row, col } = position
  const candidate = forest[row][col]
  const trees = findTreesInDirection(forest, position, direction)
  const index = trees.findIndex((tree) => tree >= candidate)
  if (index === -1) {
    return trees.length
  } else {
    return index + 1
  }
}

assert.strictEqual(distance(testForest, new Position(1, 2), Direction.Up), 1)
assert.strictEqual(distance(testForest, new Position(1, 2), Direction.Left), 1)
assert.strictEqual(distance(testForest, new Position(1, 2), Direction.Right), 2)
assert.strictEqual(distance(testForest, new Position(1, 2), Direction.Down), 2)
assert.strictEqual(distance(testForest, new Position(3, 2), Direction.Up), 2)
assert.strictEqual(distance(testForest, new Position(3, 2), Direction.Left), 2)
assert.strictEqual(distance(testForest, new Position(3, 2), Direction.Down), 1)
assert.strictEqual(distance(testForest, new Position(3, 2), Direction.Right), 2)

function score(forest: Forest, position: Position) {
  return directions
    .map((direction) => distance(forest, position, direction))
    .reduce((a, b) => a * b)
}

function highestScore(forest: Forest) {
  let highest = 0
  for (let row = 0; row < forest.length; row++) {
    for (let col = 0; col < forest[row].length; col++) {
      const currentScore = score(forest, new Position(row, col))
      if (currentScore > highest) highest = currentScore
    }
  }
  return highest
}

assert.strictEqual(highestScore(testForest), 8)

console.log(highestScore(Forest.parse(await input(8))))
