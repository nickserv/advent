import assert from "assert"
import { input, sum } from "./util.js"

class File {
  constructor(public name: string, public size: number) {}
}

class Dir {
  contents: (File | Dir)[]

  constructor(public name: string, ...contents: (File | Dir)[]) {
    this.contents = contents
  }

  size(): number {
    return sum(
      this.contents.map((value) =>
        value instanceof Dir ? value.size() : value.size,
      ),
    )
  }
}

type Command = string | (File | Dir)[]

function parseCommands(input: string) {
  return [
    ...input.matchAll(/\$ (\w+)(?: (\w+|\/|..))?(?:\n([\w\s\.]+))?/g),
  ].map(([, name, path, output]): Command => {
    switch (name) {
      case "cd":
        return path
      case "ls":
        return [...output.matchAll(/(dir|\d+) (.+)/g)].map(
          ([, dirOrSize, name]) =>
            dirOrSize === "dir"
              ? new Dir(name)
              : new File(name, parseInt(dirOrSize)),
        )
      default:
        throw new Error(`Unknown command ${name}`)
    }
  })
}

const testOutput = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`
assert.deepStrictEqual(parseCommands(testOutput), [
  "/",
  [
    new Dir("a"),
    new File("b.txt", 14848514),
    new File("c.dat", 8504156),
    new Dir("d"),
  ],
  "a",
  [
    new Dir("e"),
    new File("f", 29116),
    new File("g", 2557),
    new File("h.lst", 62596),
  ],
  "e",
  [new File("i", 584)],
  "..",
  "..",
  "d",
  [
    new File("j", 4060174),
    new File("d.log", 8033020),
    new File("d.ext", 5626152),
    new File("k", 7214296),
  ],
] satisfies Command[])

function tree(commands: Command[]) {
  const stack: Dir[] = []
  for (const command of commands) {
    if (typeof command === "string") {
      if (command === "..") stack.pop()
      else {
        const dir = new Dir(command)
        stack.at(-1)?.contents.push(dir)
        stack.push(dir)
      }
    } else {
      stack.at(-1)!.contents = command.filter((value) => value instanceof File)
    }
  }
  return stack[0]
}

// assert.deepStrictEqual(
//   tree(parseCommands(testOutput)),
//   new Dir(
//     "/",
//     new Dir(
//       "a",
//       new Dir("e", new File("i", 584)),
//       new File("f", 29116),
//       new File("g", 2557),
//       new File("h.lst", 62596),
//     ),
//     new File("b.txt", 14848514),
//     new File("c.dat", 8504156),
//     new Dir(
//       "d",
//       new File("j", 4060174),
//       new File("d.log", 8033020),
//       new File("d.ext", 5626152),
//       new File("k", 7214296),
//     ),
//   ),
// )

function dirs(dir: Dir): Dir[] {
  return dir.contents.flatMap((value) =>
    value instanceof Dir ? dirs(value).concat(value) : [],
  )
}

function sumDirs(dir: Dir) {
  const limit = 100_000

  return sum(
    dirs(dir)
      .map((dir) => dir.size())
      .filter((size) => size <= limit),
  )
}

assert.deepStrictEqual(sumDirs(tree(parseCommands(testOutput))), 95_437)

console.log(sumDirs(tree(parseCommands(await input(7)))))

function bestDirSize(dir: Dir) {
  const total = 70_000_000
  const required = 30_000_000
  const needed = dir.size() + required - total

  return Math.min(
    ...dirs(dir)
      .map((dir) => dir.size())
      .filter((size) => size >= needed),
  )
}

assert.deepStrictEqual(bestDirSize(tree(parseCommands(testOutput))), 24_933_642)

console.log(bestDirSize(tree(parseCommands(await input(7)))))
