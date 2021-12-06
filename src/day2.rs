use std::{
    fmt::{Display, Formatter, Result},
    fs::read_to_string,
};

struct PositionAndDepth {
    position: i32,
    depth: i32,
}

impl PositionAndDepth {
    fn new() -> Self {
        Self {
            position: 0,
            depth: 0,
        }
    }
}

impl Display for PositionAndDepth {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(f, "{}", self.position * self.depth)
    }
}

fn part_1(lines: &[(String, i32)]) -> PositionAndDepth {
    let mut position_and_depth = PositionAndDepth::new();

    for (direction, amount) in lines {
        match direction.as_str() {
            "forward" => position_and_depth.position += amount,
            "down" => position_and_depth.depth += amount,
            "up" => position_and_depth.depth -= amount,
            _ => unreachable!(),
        }
    }

    position_and_depth
}

fn part_2(lines: &[(String, i32)]) -> PositionAndDepth {
    let mut position_and_depth = PositionAndDepth::new();
    let mut aim = 0;

    for (direction, amount) in lines {
        match direction.as_str() {
            "forward" => {
                position_and_depth.position += amount;
                position_and_depth.depth += aim * amount;
            }
            "down" => aim += amount,
            "up" => aim -= amount,
            _ => unreachable!(),
        }
    }

    position_and_depth
}

pub fn main() {
    let lines: Vec<(String, i32)> = read_to_string("resources/2.txt")
        .unwrap()
        .lines()
        .map(|line| {
            let mut split = line.split(' ');
            (
                split.next().unwrap().to_string(),
                split.next().unwrap().parse().unwrap(),
            )
        })
        .collect();

    println!("{}", part_1(&lines));
    println!("{}", part_2(&lines));
}
