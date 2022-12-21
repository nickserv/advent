import assert from "assert/strict"
import { input } from "./util.js"

type Operator = "+" | "-" | "*" | "/"

interface OperationDeclaration {
  type: Operator
  left: string
  right: string
}

type InstructionDeclaration = number | OperationDeclaration

interface Operation {
  type: Operator
  left: Instruction
  right: Instruction
}

type Instruction = number | Operation

function parseInstructions(input: string) {
  const declarationMap = new Map(
    input.split("\n").map((line) => {
      const [register, value] = line.split(": ")
      const instruction: InstructionDeclaration = parseInt(value) || {
        type: value[5] as Operator,
        left: value.slice(0, 4),
        right: value.slice(7),
      }
      return [register, instruction]
    }),
  )
  const map = new Map<
    string,
    | number
    | {
        type: Operator
        left?: Instruction
        right?: Instruction
      }
  >(
    [...declarationMap].map(([register, instruction]) => {
      if (typeof instruction === "number") {
        return [register, instruction]
      } else {
        return [register, { type: instruction.type }]
      }
    }),
  )
  for (const [register, value] of map) {
    const declaration = declarationMap.get(register)!
    if (typeof value !== "number" && typeof declaration !== "number") {
      value.left = map.get(declaration.left) as Operation
      value.right = map.get(declaration.right) as Operation
    }
  }
  return map as Map<string, Instruction>
}

function evaluate(instruction: Instruction): number {
  if (typeof instruction === "number") {
    return instruction
  } else {
    const { type, left, right } = instruction
    switch (type) {
      case "+":
        return evaluate(left) + evaluate(right)
      case "-":
        return evaluate(left) - evaluate(right)
      case "*":
        return evaluate(left) * evaluate(right)
      case "/":
        return evaluate(left) / evaluate(right)
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
assert.equal(evaluate(testInstructions.get("root")!), 152)

const instructions = parseInstructions(await input(21))
console.log(evaluate(instructions.get("root")!))
