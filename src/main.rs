use std::fs::File;
use std::io::prelude::*;
use std::io::Result;

fn read_numbers() -> Result<Vec<u32>> {
    let mut file = File::open("resources/1.txt")?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;
    Ok(buf
        .lines()
        .map(|line| line.parse().unwrap())
        .collect::<Vec<u32>>())
}

fn find_double_product(numbers: &[u32]) -> Option<u32> {
    let mut i = 0;
    while i < numbers.len() {
        let mut j = i + 1;
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

fn find_triple_product(numbers: &[u32]) -> Option<u32> {
    let mut i = 0;
    while i < numbers.len() {
        let mut j = i + 1;
        while j < numbers.len() {
            let mut k = j + 1;
            while k < numbers.len() {
                let sum = numbers[i] + numbers[j] + numbers[k];
                if sum == 2020 {
                    let product = numbers[i] * numbers[j] * numbers[k];
                    return Some(product);
                }
                k += 1;
            }
            j += 1;
        }
        i += 1;
    }
    None
}

fn main() -> Result<()> {
    let numbers = read_numbers()?;
    println!("{}", find_double_product(&numbers).unwrap());
    println!("{}", find_triple_product(&numbers).unwrap());
    Ok(())
}
