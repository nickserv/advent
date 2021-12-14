use itertools::{Itertools, MinMaxResult::MinMax};
use std::{collections::HashMap, convert::Infallible, fs::read_to_string, str::FromStr};

#[derive(Debug, PartialEq)]
struct Rule {
    left: char,
    right: char,
    insertion: char,
}

impl FromStr for Rule {
    type Err = Infallible;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let chars: Vec<char> = s.chars().collect();

        Ok(Self {
            left: chars[0],
            right: chars[1],
            insertion: chars[6],
        })
    }
}

#[test]
fn test_parse_rule() {
    let rule: Rule = "CH -> B".parse().unwrap();
    assert_eq!(
        rule,
        Rule {
            left: 'C',
            right: 'H',
            insertion: 'B'
        }
    );
}

struct Instructions {
    template: String,
    rules: HashMap<(char, char), char>,
}

impl Instructions {
    fn quantity_difference(&self, steps: u8) -> usize {
        let mut template = self.template.clone();
        for _ in 0..steps {
            let insertions: String = template
                .chars()
                .tuple_windows::<(_, _)>()
                .map(|window| self.rules.get(&window).unwrap())
                .collect();
            template = template.chars().interleave(insertions.chars()).collect();
        }
        match template.chars().counts().values().minmax() {
            MinMax(min, max) => max - min,
            _ => unreachable!(),
        }
    }
}

#[test]
fn test_quantity_difference() {
    let instructions: Instructions = "NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"
        .parse()
        .unwrap();
    assert_eq!(instructions.quantity_difference(10), 1588);
}

#[derive(Debug)]
enum ParseInstructionsError {
    NoDelimiterError,
}

impl FromStr for Instructions {
    type Err = ParseInstructionsError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (template, rules) = s.split_once("\n\n").ok_or(Self::Err::NoDelimiterError)?;

        Ok(Self {
            template: template.to_string(),
            rules: rules
                .lines()
                .map(|line| {
                    let rule: Rule = line.parse().unwrap();
                    ((rule.left, rule.right), rule.insertion)
                })
                .collect(),
        })
    }
}

pub fn main() {
    let instructions: Instructions = read_to_string("resources/14.txt").unwrap().parse().unwrap();
    println!("{}", instructions.quantity_difference(10));
}
