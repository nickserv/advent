use std::fs::read_to_string;

fn parse_numbers() -> Vec<u32> {
    read_to_string("resources/1.txt")
        .unwrap()
        .lines()
        .flat_map(|line| line.parse())
        .collect()
}

fn count_comparisons(numbers: &[u32]) -> usize {
    numbers
        .windows(2)
        .filter(|window| window[1] > window[0])
        .count()
}

pub fn main() {
    let numbers = parse_numbers();
    println!("{}", count_comparisons(&numbers));
}
