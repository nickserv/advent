use itertools::Itertools;
use std::collections::HashSet;
use std::fs::read_to_string;

fn parse_answer_groups() -> Vec<Vec<HashSet<char>>> {
    read_to_string("resources/6.txt")
        .unwrap()
        .split("\n\n")
        .map(|str| {
            str.trim()
                .split('\n')
                .map(|str| str.chars().filter(|c| c.is_alphabetic()).collect())
                .collect()
        })
        .collect()
}

fn sum_unions(answer_groups: &Vec<Vec<HashSet<char>>>) -> usize {
    answer_groups
        .iter()
        .map(|answer_group| {
            answer_group
                .iter()
                .cloned()
                .fold1(|previous, next| previous.union(&next).cloned().collect())
                .unwrap()
                .len()
        })
        .sum()
}

fn sum_intersections(answer_groups: &Vec<Vec<HashSet<char>>>) -> usize {
    answer_groups
        .iter()
        .map(|answer_group| {
            answer_group
                .iter()
                .cloned()
                .fold1(|previous, next| previous.intersection(&next).cloned().collect())
                .unwrap()
                .len()
        })
        .sum()
}

pub fn main() {
    let answer_groups = parse_answer_groups();
    println!("{}", sum_unions(&answer_groups));
    println!("{}", sum_intersections(&answer_groups));
}
