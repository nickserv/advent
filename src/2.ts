import assert from "assert/strict";
import { readFile } from "fs/promises";
import { input, sum } from "./util.js";

enum Shape {
	Rock,
	Paper,
	Scissors,
}

const shapes = new Map([
	["A", Shape.Rock],
	["B", Shape.Paper],
	["C", Shape.Scissors],
	["X", Shape.Rock],
	["Y", Shape.Paper],
	["Z", Shape.Scissors],
]);

const winners = new Map([
	[Shape.Rock, Shape.Paper],
	[Shape.Paper, Shape.Scissors],
	[Shape.Scissors, Shape.Rock],
]);

function score1(otherShape: Shape, myShape: Shape) {
	const shapeScore = new Map([
		[Shape.Rock, 1],
		[Shape.Paper, 2],
		[Shape.Scissors, 3],
	]).get(myShape)!;
	if (winners.get(otherShape) === myShape) {
		return shapeScore + 6;
	} else if (otherShape === myShape) {
		return shapeScore + 3;
	} else {
		return shapeScore;
	}
}

assert.equal(score1(Shape.Rock, Shape.Paper), 8);
assert.equal(score1(Shape.Paper, Shape.Rock), 1);
assert.equal(score1(Shape.Scissors, Shape.Scissors), 6);

console.log(
	sum(
		(await readFile("resources/2.txt", "utf8"))
			.trim()
			.split("\n")
			.map(([otherShape, , myShape]) =>
				score1(shapes.get(otherShape)!, shapes.get(myShape)!),
			),
	),
);

enum Result {
	Win,
	Draw,
	Lose,
}

const results = new Map([
	["X", Result.Lose],
	["Y", Result.Draw],
	["Z", Result.Win],
]);

function score2(otherShape: Shape, result: Result) {
	const myShape = new Map([
		[Result.Win, winners.get(otherShape)!],
		[Result.Draw, otherShape],
		[Result.Lose, winners.get(winners.get(otherShape)!)!],
	]).get(result)!;
	const shapeScore = new Map([
		[Shape.Rock, 1],
		[Shape.Paper, 2],
		[Shape.Scissors, 3],
	]).get(myShape)!;
	if (result === Result.Win) {
		return shapeScore + 6;
	} else if (result === Result.Draw) {
		return shapeScore + 3;
	} else {
		return shapeScore;
	}
}

assert.equal(score2(Shape.Rock, Result.Draw), 4);
assert.equal(score2(Shape.Paper, Result.Lose), 1);
assert.equal(score2(Shape.Scissors, Result.Win), 7);

console.log(
	sum(
		(await input(2))
			.split("\n")
			.map(([otherShape, , result]) =>
				score2(shapes.get(otherShape)!, results.get(result)!),
			),
	),
);
