import { readdir } from "fs/promises"
import { basename, extname } from "path"

const files = await readdir("src")
await Promise.all(
  files.map(async (path) => {
    const day = parseInt(basename(path, extname(path)))
    if (day) await import(`./${day}.js`)
  }),
)
