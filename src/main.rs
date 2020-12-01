use std::fs::File;
use std::io;
use std::io::prelude::*;

fn main() -> io::Result<()> {
    let mut file = File::open("resources/1.txt")?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;

    let numbers = buf
        .lines()
        .map(|line| line.parse().unwrap())
        .collect::<Vec<u32>>();

    let mut i = 0;
    while i < numbers.len() {
        let mut j = i;
        while j < numbers.len() {
            let sum = numbers[i] + numbers[j];
            if sum == 2020 {
                let product = numbers[i] * numbers[j];
                println!("{}", product);
            }
            j += 1;
        }
        i += 1;
    }

    Ok(())
}
