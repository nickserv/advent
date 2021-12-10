#![allow(clippy::ptr_arg)]
use std::fs::read_to_string;

#[cfg(test)]
lazy_static! {
    static ref TEST_MAP: Vec<Vec<u8>> = "2199943210
3987894921
9856789892
8767896789
9899965678"
        .lines()
        .map(|line| {
            line.chars()
                .map(|char| char.to_digit(10).unwrap() as u8)
                .collect::<Vec<u8>>()
        })
        .collect();
}

fn low_points(map: &Vec<Vec<u8>>) -> Vec<u8> {
    let mut set = Vec::new();
    for (i, row) in map.iter().enumerate() {
        for (j, &current) in row.iter().enumerate() {
            let above = (i > 0).then(|| map[i - 1][j]);
            let below = (i + 1 < map.len()).then(|| map[i + 1][j]);
            let left = (j > 0).then(|| row[j - 1]);
            let right = (j + 1 < row.len()).then(|| row[j + 1]);

            if [above, below, left, right]
                .iter()
                .flatten()
                .all(|x| current < *x)
            {
                set.push(current);
            }
        }
    }
    set
}

#[test]
fn test_low_points() {
    assert_eq!(low_points(&TEST_MAP), vec![1, 0, 5, 5]);
}

fn risk_level(map: &Vec<Vec<u8>>) -> u16 {
    let low_points = low_points(map);
    low_points.iter().map(|point| *point as u16).sum::<u16>() + low_points.len() as u16
}

#[test]
fn test_risk_level() {
    assert_eq!(risk_level(&TEST_MAP), 15);
}

pub fn main() {
    let map: Vec<Vec<u8>> = read_to_string("resources/9.txt")
        .unwrap()
        .lines()
        .map(|line| {
            line.chars()
                .map(|char| char.to_digit(10).unwrap() as u8)
                .collect::<Vec<u8>>()
        })
        .collect();
    println!("{}", risk_level(&map));
}
