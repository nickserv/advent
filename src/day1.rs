use std::fs::read_to_string;

fn count_comparisons<'a, T: Iterator<Item = &'a [u32]>>(numbers: T) -> usize {
    numbers.filter(|window| window[1] > window[0]).count()
}

fn count_comparisons_1(numbers: &[u32]) -> usize {
    count_comparisons(numbers.windows(2))
}

fn count_comparisons_2(numbers: &[u32]) -> usize {
    count_comparisons(
        numbers
            .windows(3)
            .map(|window| window.iter().sum())
            .collect::<Vec<_>>()
            .windows(2),
    )
}

pub fn main() {
    let numbers: Vec<u32> = read_to_string("resources/1.txt")
        .unwrap()
        .lines()
        .flat_map(|line| line.parse())
        .collect();

    println!("{}", count_comparisons_1(&numbers));
    println!("{}", count_comparisons_2(&numbers));
}
