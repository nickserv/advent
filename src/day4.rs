use std::collections::HashMap;
use std::fs::read_to_string;

fn parse_passports() -> Vec<HashMap<String, String>> {
    read_to_string("resources/4.txt")
        .unwrap()
        .split("\n\n")
        .map(|string| {
            let mut passport = HashMap::new();
            for string in string.split_whitespace() {
                let mut iter = string.split(':');
                passport.insert(
                    iter.next().unwrap().to_string(),
                    iter.next().unwrap().to_string(),
                );
            }
            passport
        })
        .collect()
}

fn validate_presence(passport: &HashMap<String, String>) -> bool {
    ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        .iter()
        .all(|key| passport.contains_key(&key.to_string()))
}

fn validate_specification(passport: &HashMap<String, String>) -> bool {
    let mut specification: HashMap<&str, fn(&str) -> bool> = HashMap::new();
    specification.insert("byr", |str| matches!(str.parse().unwrap(), 1920..=2002));
    specification.insert("iyr", |str| matches!(str.parse().unwrap(), 2010..=2020));
    specification.insert("eyr", |str| matches!(str.parse().unwrap(), 2020..=2030));
    specification.insert("hgt", |str| {
        (str.ends_with("cm") && matches!(str[..str.len() - 2].parse().unwrap(), 150..=193))
            || (str.ends_with("in") && matches!(str[..str.len() - 2].parse().unwrap(), 59..=76))
    });
    specification.insert("hcl", |str| {
        str.len() == 7
            && str.starts_with('#')
            && str[1..].chars().all(|char| char.is_ascii_hexdigit())
    });
    specification.insert("ecl", |str| {
        ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&str)
    });
    specification.insert("pid", |str| {
        str.len() == 9 && str.chars().all(|char| char.is_digit(10))
    });

    specification.iter().all(|(key, validate)| {
        passport.contains_key(&key.to_string()) && validate(passport[&key.to_string()].as_str())
    })
}

fn count_valid(
    passports: &[HashMap<String, String>],
    validate: fn(&HashMap<String, String>) -> bool,
) -> usize {
    passports.iter().cloned().filter(validate).count()
}

pub fn main() {
    let passports = parse_passports();
    println!("{}", count_valid(&passports, validate_presence));
    println!("{}", count_valid(&passports, validate_specification));
}
