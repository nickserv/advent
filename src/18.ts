import assert from "assert/strict";
import { input } from "./util.js";

class Position {
	constructor(
		public x: number,
		public y: number,
		public z: number,
	) {}

	static parse(input: string) {
		return input.split("\n").map((line) => {
			const [x, y, z] = line.split(",").map((number) => parseInt(number));
			return new Position(x, y, z);
		});
	}

	get adjacent() {
		return [
			new Position(this.x - 1, this.y, this.z),
			new Position(this.x + 1, this.y, this.z),
			new Position(this.x, this.y - 1, this.z),
			new Position(this.x, this.y + 1, this.z),
			new Position(this.x, this.y, this.z - 1),
			new Position(this.x, this.y, this.z + 1),
		];
	}
}

class Grid {
	value: boolean[][][] = [];

	constructor(positions: Position[]) {
		for (const { x, y, z } of positions) {
			this.value[x] ||= [];
			this.value[x][y] ||= [];
			this.value[x][y][z] = true;
		}
	}

	get surfaceArea() {
		let count = 0;
		for (const x of this.value.keys()) {
			if (this.value[x]) {
				for (const y of this.value[x].keys()) {
					if (this.value[x][y]) {
						for (const z of this.value[x][y].keys()) {
							if (this.value[x][y][z]) {
								const adjacent = new Position(x, y, z).adjacent.filter(
									({ x, y, z }) => this.value[x]?.[y]?.[z],
								).length;
								count += 6 - adjacent;
							}
						}
					}
				}
			}
		}
		return count;
	}
}

const testGrid = new Grid(
	Position.parse(`2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5`),
);
assert.equal(testGrid.surfaceArea, 64);

const grid = new Grid(Position.parse(await input(18)));
console.log(grid.surfaceArea);
