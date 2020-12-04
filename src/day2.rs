use regex::Regex;
use std::fs::read_to_string;

#[derive(Clone)]
struct Specification {
    start: usize,
    end: usize,
    letter: char,
    password: String,
}

fn parse_specifications() -> Vec<Specification> {
    let re = Regex::new(r"(?P<start>\d+)-(?P<end>\d+) (?P<letter>\w): (?P<password>\w+)").unwrap();
    read_to_string("resources/2.txt")
        .unwrap()
        .lines()
        .flat_map(|line| re.captures(line))
        .map(|captures| Specification {
            start: captures["start"].parse().unwrap(),
            end: captures["end"].parse().unwrap(),
            letter: captures["letter"].chars().next().unwrap(),
            password: captures["password"].to_string(),
        })
        .collect()
}

fn validate_count(specification: &Specification) -> bool {
    let count = specification
        .password
        .chars()
        .filter(|c| c == &specification.letter)
        .count();
    count >= specification.start && count <= specification.end
}

fn xor(a: bool, b: bool) -> bool {
    if a {
        !b
    } else {
        b
    }
}

fn validate_positions(specification: &Specification) -> bool {
    xor(
        specification
            .password
            .chars()
            .nth(specification.start - 1)
            .unwrap()
            == specification.letter,
        specification
            .password
            .chars()
            .nth(specification.end - 1)
            .unwrap()
            == specification.letter,
    )
}

fn count_valid(specifications: &[Specification], validate: fn(&Specification) -> bool) -> usize {
    specifications.iter().cloned().filter(validate).count()
}

pub fn main() {
    let specifications = parse_specifications();
    println!("{}", count_valid(&specifications, validate_count));
    println!("{}", count_valid(&specifications, validate_positions));
}
