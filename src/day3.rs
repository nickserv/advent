#![allow(clippy::needless_range_loop, clippy::ptr_arg)]
use std::fs::read_to_string;

fn power_consumption(lines: &Vec<String>) -> u32 {
    let len = lines[0].len();
    let mut counts: Vec<i8> = vec![0; len];
    for i in 0..len {
        for line in lines {
            if line.chars().nth(i).unwrap() == '1' {
                counts[i] += 1;
            } else {
                counts[i] -= 1;
            }
        }
    }
    let gamma_rate = u16::from_str_radix(
        counts
            .iter()
            .map(|x| if *x >= 0 { '1' } else { '0' })
            .collect::<String>()
            .as_str(),
        2,
    )
    .unwrap();
    let epsilon_rate = u16::from_str_radix(
        counts
            .iter()
            .map(|x| if *x < 0 { '1' } else { '0' })
            .collect::<String>()
            .as_str(),
        2,
    )
    .unwrap();
    gamma_rate as u32 * epsilon_rate as u32
}

#[test]
fn test_power_consumption() {
    let lines: Vec<String> = parse(read_to_string("resources/3test.txt").unwrap());
    assert_eq!(power_consumption(&lines), 198);
}

fn parse(string: String) -> Vec<String> {
    string.lines().map(|line| line.chars().collect()).collect()
}

pub fn main() {
    let lines: Vec<String> = parse(read_to_string("resources/3.txt").unwrap());
    println!("{}", power_consumption(&lines));
}
