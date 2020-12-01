use std::fs::File;
use std::io;
use std::io::prelude::*;

fn read_numbers() -> io::Result<Vec<u32>> {
    let mut file = File::open("resources/1.txt")?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;
    Ok(buf
        .lines()
        .map(|line| line.parse().unwrap())
        .collect::<Vec<u32>>())
}

fn find_product(numbers: Vec<u32>) -> Option<u32> {
    let mut i = 0;
    while i < numbers.len() {
        let mut j = i;
        while j < numbers.len() {
            let sum = numbers[i] + numbers[j];
            if sum == 2020 {
                let product = numbers[i] * numbers[j];
                return Some(product);
            }
            j += 1;
        }
        i += 1;
    }
    None
}

fn main() -> io::Result<()> {
    let numbers = read_numbers()?;
    println!("{}", find_product(numbers).unwrap());
    Ok(())
}
