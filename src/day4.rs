#![allow(clippy::ptr_arg)]
use std::fs::read_to_string;

type Board = Vec<Vec<u8>>;
type Marking = Vec<Vec<bool>>;

fn is_winner(marks: &Marking) -> bool {
    let row_winner = marks.iter().any(|row| row.iter().all(|&mark| mark));
    let column_winner = (0..5).any(|i| marks.iter().all(|row| row[i]));
    row_winner || column_winner
}

fn unmarked_sum(board: &Board, marking: &Marking) -> u16 {
    let mut sum: u16 = 0;
    for (row_index, row) in board.iter().enumerate() {
        for (col_index, col) in row.iter().enumerate() {
            if !marking[row_index][col_index] {
                sum += *col as u16;
            }
        }
    }
    sum
}

fn bingo_winners(numbers: &[u8], boards: &[Board]) -> Vec<u32> {
    let mut markings = vec![vec![vec![false; 5]; 5]; boards.len()];
    let mut winners: Vec<usize> = Vec::new();
    let mut scores: Vec<u32> = Vec::new();
    for number in numbers {
        for (board_index, board) in boards.iter().enumerate() {
            for (row_index, row) in board.iter().enumerate() {
                for (col_index, col) in row.iter().enumerate() {
                    if col == number {
                        markings[board_index][row_index][col_index] = true;
                    }
                }
            }

            if is_winner(&markings[board_index]) && !winners.contains(&board_index) {
                winners.push(board_index);
                scores.push(unmarked_sum(board, &markings[board_index]) as u32 * *number as u32);
            }
        }
    }
    scores
}

#[test]
fn test_bingo_winner() {
    let (numbers, boards) = parse(read_to_string("resources/4test.txt").unwrap());
    assert_eq!(*bingo_winners(&numbers, &boards).first().unwrap(), 4512);
    assert_eq!(*bingo_winners(&numbers, &boards).last().unwrap(), 1924);
}

fn parse(string: String) -> (Vec<u8>, Vec<Board>) {
    let mut sections = string.split("\n\n");
    let first = sections.next().unwrap();

    let numbers: Vec<u8> = first.split(',').map(|char| char.parse().unwrap()).collect();
    let boards: Vec<Board> = sections
        .map(|section| {
            section
                .lines()
                .map(|line| {
                    line.split_whitespace()
                        .map(|s| s.parse().unwrap())
                        .collect()
                })
                .collect()
        })
        .collect();

    (numbers, boards)
}

pub fn main() {
    let (numbers, boards) = parse(read_to_string("resources/4.txt").unwrap());
    println!("{}", bingo_winners(&numbers, &boards).first().unwrap());
    println!("{}", bingo_winners(&numbers, &boards).last().unwrap());
}
