use std::fs::read_to_string;

fn parse_map() -> Vec<Vec<bool>> {
    read_to_string("resources/3.txt")
        .unwrap()
        .lines()
        .map(|line| line.chars().map(|char| char == '#').collect())
        .collect()
}

fn count(map: &[Vec<bool>], horizontal_offset: usize, vertical_offset: usize) -> u32 {
    let mut vertical = 0;
    let mut horizontal = 0;
    let mut count = 0;

    while vertical < map.len() {
        let row = &map[vertical];

        if row[horizontal] {
            count += 1;
        }

        if horizontal + horizontal_offset > row.len() - 1 {
            horizontal = horizontal + horizontal_offset - row.len()
        } else {
            horizontal += horizontal_offset
        }

        vertical += vertical_offset
    }

    count
}

pub fn main() {
    let map = parse_map();
    println!("{}", count(&map, 3, 1));
    println!(
        "{}",
        count(&map, 1, 1)
            * count(&map, 3, 1)
            * count(&map, 5, 1)
            * count(&map, 7, 1)
            * count(&map, 1, 2)
    );
}
