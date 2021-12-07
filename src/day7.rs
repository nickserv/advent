use std::fs::read_to_string;

#[cfg(test)]
const TEST_POSITIONS: &[i32] = &[16, 1, 2, 0, 4, 2, 7, 1, 2, 14];

fn median(list: Vec<i32>) -> i32 {
    let mut sorted_list = list.clone();
    sorted_list.sort_unstable();
    sorted_list[list.len() / 2]
}

#[test]
fn test_median() {
    assert_eq!(median(TEST_POSITIONS.to_vec()), 2);
}

fn distance(list: &[i32]) -> i32 {
    let list_median = median(list.to_vec());
    let distances = list.iter().map(|n| (n - list_median).abs());
    distances.sum()
}

#[test]
fn test_distance() {
    assert_eq!(distance(TEST_POSITIONS), 37);
}

pub fn main() {
    let positions: Vec<i32> = read_to_string("resources/7.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|fish| fish.parse().unwrap())
        .collect();

    println!("{}", distance(&positions));
}
