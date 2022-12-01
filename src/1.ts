import { readFile } from "fs/promises"

async function parseCalories(): Promise<number[][]> {
  return (await readFile("resources/1.txt", "utf8")).split("\n\n").map((str) =>
    str
      .trim()
      .split("\n")
      .map((str) => {
        if (isNaN(parseInt(str))) throw new Error(`Invalid number: ${str}`)
        else return parseInt(str)
      }),
  )
}

console.log(
  Math.max(
    ...(await parseCalories()).map((elf) => elf.reduce((a, b) => a + b)),
  ),
)

console.log(
  (await parseCalories())
    .map((elf) => elf.reduce((a, b) => a + b))
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((a, b) => a + b),
)
