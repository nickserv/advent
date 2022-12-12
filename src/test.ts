import { readdir } from "fs/promises"
import { basename, extname } from "path"

const days = (await readdir("src"))
  .map((path) => parseInt(basename(path, extname(path))))
  .filter((day) => day)
  .sort((a, b) => a - b)

for (const day of days) await import(`./${day}.js`)
