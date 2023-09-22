import { readdir } from "fs/promises";
import { basename, extname } from "path";

await Promise.all(
	(await readdir("src")).map(async (path) => {
		const day = parseInt(basename(path, extname(path)));
		if (day) await import(`./${day}.js`);
	}),
);
