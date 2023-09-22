import { readFile } from "fs/promises";

export async function input(day: number) {
	return (await readFile(`resources/${day}.txt`, "utf8")).trimEnd();
}

export function sum(numbers: number[]) {
	return numbers.reduce((a, b) => a + b);
}
