use std::fs::read_to_string;

fn parse_numbers() -> Vec<u32> {
    read_to_string("resources/1.txt")
        .unwrap()
        .lines()
        .flat_map(|line| line.parse())
        .collect()
}

fn find_double_product(numbers: &[u32]) -> u32 {
    let mut i = 0;
    while i < numbers.len() {
        let mut j = i + 1;
        while j < numbers.len() {
            let sum = numbers[i] + numbers[j];
            if sum == 2020 {
                let product = numbers[i] * numbers[j];
                return product;
            }
            j += 1;
        }
        i += 1;
    }
    panic!("Input does not have a valid match")
}

fn find_triple_product(numbers: &[u32]) -> u32 {
    let mut i = 0;
    while i < numbers.len() {
        let mut j = i + 1;
        while j < numbers.len() {
            let mut k = j + 1;
            while k < numbers.len() {
                let sum = numbers[i] + numbers[j] + numbers[k];
                if sum == 2020 {
                    let product = numbers[i] * numbers[j] * numbers[k];
                    return product;
                }
                k += 1;
            }
            j += 1;
        }
        i += 1;
    }
    panic!("Input does not have a valid match")
}

pub fn main() {
    let numbers = parse_numbers();
    println!("{}", find_double_product(&numbers));
    println!("{}", find_triple_product(&numbers));
}
