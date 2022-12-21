import assert from "assert/strict"
import { input } from "./util.js"

type Operator = "+" | "-" | "*" | "/"

interface Operation {
  type: Operator
  left: string
  right: string
}

type Instruction = number | Operation

function parseInstructions(input: string) {
  return new Map(
    input.split("\n").map((line) => {
      const [register, value] = line.split(": ")
      const instruction: Instruction = parseInt(value) || {
        type: value[5] as Operator,
        left: value.slice(0, 4),
        right: value.slice(7),
      }
      return [register, instruction]
    }),
  )
}

function evaluate(
  instructions: Map<string, Instruction>,
  register = "root",
): number {
  const value = instructions.get(register)!
  if (typeof value === "number") {
    return value
  } else {
    const { type, left, right } = value
    switch (type) {
      case "+":
        return evaluate(instructions, left) + evaluate(instructions, right)
      case "-":
        return evaluate(instructions, left) - evaluate(instructions, right)
      case "*":
        return evaluate(instructions, left) * evaluate(instructions, right)
      case "/":
        return evaluate(instructions, left) / evaluate(instructions, right)
    }
  }
}

const testInstructions = parseInstructions(`root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32`)
assert.equal(evaluate(testInstructions), 152)

const instructions = parseInstructions(await input(21))
console.log(evaluate(instructions))
