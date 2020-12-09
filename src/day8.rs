use std::collections::HashSet;
use std::fs::read_to_string;

#[derive(Debug)]
struct Instruction {
    operation: String,
    argument: i16,
}

fn parse_instructions() -> Vec<Instruction> {
    read_to_string("resources/8.txt")
        .unwrap()
        .lines()
        .map(|line| {
            let mut iter = line.split_whitespace();

            Instruction {
                operation: iter.next().unwrap().to_owned(),
                argument: iter.next().unwrap().parse().unwrap(),
            }
        })
        .collect()
}

fn run_instructions(instructions: &[Instruction]) -> i16 {
    let mut visited = HashSet::new();
    let mut index = 0;
    let mut accumulator = 0;

    while !visited.contains(&index) && index < instructions.len() {
        visited.insert(index);
        let Instruction {
            operation,
            argument,
        } = &instructions[index];

        match operation.as_str() {
            "acc" => {
                accumulator += argument;
                index += 1;
            }
            "jmp" => index = (index as isize + *argument as isize) as usize,
            "nop" => index += 1,
            _ => unreachable!(),
        };
    }

    accumulator
}

pub fn main() {
    let instructions = parse_instructions();
    println!("{}", run_instructions(&instructions));
}
