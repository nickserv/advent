use regex::Regex;
use std::collections::HashMap;
use std::fs::read_to_string;

type BagMap<T> = HashMap<String, T>;

fn parse_bags() -> BagMap<BagMap<u32>> {
    let bags_regex = Regex::new(r"(?P<color>.+) bags contain (?P<contents>.+).").unwrap();
    let bag_regex = Regex::new(r"(?P<quantity>\d+) (?P<color>.+) bags?").unwrap();
    let mut bags = HashMap::new();

    for captures in bags_regex.captures_iter(read_to_string("resources/7.txt").unwrap().as_str()) {
        let mut bag = HashMap::new();

        for line in captures["contents"].split(", ") {
            bag_regex.captures(line).and_then(|captures| {
                bag.insert(
                    captures["color"].to_owned(),
                    captures["quantity"].parse().unwrap(),
                )
            });
        }

        bags.insert(captures["color"].to_owned(), bag);
    }

    bags
}

fn count_bags_containing(bags: &BagMap<BagMap<u32>>, bag: &str) -> usize {
    bags.keys()
        .filter(|key| bag_contains_bag(bags, key, bag))
        .count()
}

fn bag_contains_bag(bags: &BagMap<BagMap<u32>>, outer: &str, inner: &str) -> bool {
    bags[outer]
        .keys()
        .any(|key| key == inner || bag_contains_bag(bags, key, inner))
}

fn count_total_bags(bags: &BagMap<BagMap<u32>>, bag: &str) -> u32 {
    bags[bag]
        .iter()
        .map(|(bag, quantity)| quantity + quantity * count_total_bags(bags, bag))
        .sum()
}

pub fn main() {
    let bags = parse_bags();
    let bag = "shiny gold";
    println!("{}", count_bags_containing(&bags, bag));
    println!("{}", count_total_bags(&bags, bag));
}
