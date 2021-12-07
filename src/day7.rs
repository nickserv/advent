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

fn average(list: Vec<i32>) -> i32 {
    let result = list.iter().map(|n| *n as f64).sum::<f64>() / list.len() as f64;
    result.round() as i32
}

#[test]
fn test_average() {
    assert_eq!(average(TEST_POSITIONS.to_vec()), 5);
}

fn distance_1(positions: &[i32]) -> i32 {
    let list_median = median(positions.to_vec());
    let distances = positions.iter().map(|n| (n - list_median).abs());
    distances.sum()
}

#[test]
fn test_distance_1() {
    assert_eq!(distance_1(TEST_POSITIONS), 37);
}

fn triangle(n: i32) -> i32 {
    (n.pow(2) + n) / 2
}

fn distance_2(positions: &[i32]) -> i32 {
    let list_average = average(positions.to_vec());
    [list_average - 1, list_average, list_average + 1]
        .iter()
        .map(|position| {
            let distances = positions.iter().map(|n| triangle((n - position).abs()));
            distances.sum()
        })
        .min()
        .unwrap()
}

#[test]
fn test_distance_2() {
    assert_eq!(distance_2(TEST_POSITIONS), 168);
}

pub fn main() {
    let positions: Vec<i32> = read_to_string("resources/7.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|position| position.parse().unwrap())
        .collect();

    println!("{}", distance_1(&positions));
    println!("{}", distance_2(&positions));
}
