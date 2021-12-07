use std::fs::read_to_string;

fn simulate(fish_counts: [i64; 9], days: i16) -> i64 {
    let mut fish_counts = fish_counts;
    for _ in 0..days {
        let new_fish = fish_counts[0];
        fish_counts.rotate_left(1);
        fish_counts[6] += new_fish;
        fish_counts[8] = new_fish;
    }
    fish_counts.iter().sum()
}

pub fn main() {
    let fish_ages: Vec<usize> = read_to_string("resources/6.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|fish| fish.parse().unwrap())
        .collect();

    let mut fish_counts = [0; 9];
    for fish_age in fish_ages {
        fish_counts[fish_age] += 1;
    }

    println!("{}", simulate(fish_counts, 80));
    println!("{}", simulate(fish_counts, 256));
}
