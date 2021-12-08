use itertools::Itertools;
use std::{
    collections::{HashMap, HashSet},
    fs::read_to_string,
    str::FromStr,
};

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
enum Segment {
    Top,
    Middle,
    Bottom,
    UpperLeft,
    UpperRight,
    LowerLeft,
    LowerRight,
}

impl Segment {
    const VALUES: [Self; 7] = [
        Self::Top,
        Self::Middle,
        Self::Bottom,
        Self::UpperLeft,
        Self::UpperRight,
        Self::LowerLeft,
        Self::LowerRight,
    ];
}

#[derive(Debug)]
struct Entry {
    patterns: Vec<String>,
    output: Vec<String>,
}

#[derive(Debug)]
enum FromStrError {
    NoDelimiterError,
}

impl FromStr for Entry {
    type Err = FromStrError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (point_1, point_2) = s.split_once(" | ").ok_or(Self::Err::NoDelimiterError)?;

        Ok(Self {
            patterns: point_1
                .split_whitespace()
                .map(|str| str.to_string())
                .collect(),
            output: point_2
                .split_whitespace()
                .map(|str| str.to_string())
                .collect(),
        })
    }
}

fn count_digits(entries: &[Entry]) -> usize {
    let digits = [1, 4, 7, 8];
    let digit_segments = digits.map(|digit| DIGIT_SEGMENTS[digit].len());

    entries
        .iter()
        .map(|entry| {
            entry
                .output
                .iter()
                .filter(|string| digit_segments.contains(&string.len()))
                .count()
        })
        .sum()
}

#[test]
fn test_count_digits() {
    let entries: Vec<Entry> = read_to_string("resources/8test.txt")
        .unwrap()
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    assert_eq!(count_digits(&entries), 26);
}

lazy_static! {
    static ref DIGIT_SEGMENTS: [HashSet<Segment>; 10] = [
        HashSet::from([
            Segment::Top,
            Segment::Bottom,
            Segment::UpperLeft,
            Segment::UpperRight,
            Segment::LowerLeft,
            Segment::LowerRight,
        ]),
        HashSet::from([Segment::UpperRight, Segment::LowerRight]),
        HashSet::from([
            Segment::Top,
            Segment::UpperRight,
            Segment::Middle,
            Segment::LowerLeft,
            Segment::Bottom,
        ]),
        HashSet::from([
            Segment::Top,
            Segment::UpperRight,
            Segment::Middle,
            Segment::LowerRight,
            Segment::Bottom,
        ]),
        HashSet::from([
            Segment::UpperLeft,
            Segment::UpperRight,
            Segment::Middle,
            Segment::LowerRight,
        ]),
        HashSet::from([
            Segment::Top,
            Segment::UpperLeft,
            Segment::Middle,
            Segment::LowerRight,
            Segment::Bottom,
        ]),
        HashSet::from([
            Segment::Top,
            Segment::UpperLeft,
            Segment::Middle,
            Segment::LowerLeft,
            Segment::LowerRight,
            Segment::Bottom,
        ]),
        HashSet::from([Segment::Top, Segment::UpperRight, Segment::LowerRight]),
        HashSet::from([
            Segment::Top,
            Segment::Middle,
            Segment::Bottom,
            Segment::UpperLeft,
            Segment::UpperRight,
            Segment::LowerLeft,
            Segment::LowerRight,
        ]),
        HashSet::from([
            Segment::Top,
            Segment::Middle,
            Segment::Bottom,
            Segment::UpperLeft,
            Segment::UpperRight,
            Segment::LowerRight,
        ]),
    ];
}

fn find_configuration(entries: &[Entry]) -> HashMap<char, Segment> {
    let mut configurations = Segment::VALUES.iter().permutations(7).map(|permutation| {
        ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            .iter()
            .zip(permutation)
            .map(|(char, segment)| (*char, *segment))
            .collect::<HashMap<char, Segment>>()
    });

    configurations
        .find(|configuration| {
            entries.iter().all(|entry| {
                entry.patterns.iter().all(|pattern| {
                    let mut set = HashSet::new();
                    for char in pattern.chars() {
                        set.insert(configuration[&char]);
                    }
                    DIGIT_SEGMENTS.contains(&set)
                })
            })
        })
        .unwrap()
}

#[test]
fn test_find_configuration() {
    let entry: Entry =
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
            .parse()
            .unwrap();

    assert_eq!(
        find_configuration(&[entry]),
        HashMap::from([
            ('a', Segment::UpperRight),
            ('b', Segment::LowerRight),
            ('c', Segment::Bottom),
            ('d', Segment::Top),
            ('e', Segment::UpperLeft),
            ('f', Segment::Middle),
            ('g', Segment::LowerLeft),
        ])
    );
}

fn sum_output(entries: &[Entry]) -> usize {
    let configuration = find_configuration(entries);

    entries
        .iter()
        .map(|entry| {
            entry
                .output
                .iter()
                .map(|string| {
                    DIGIT_SEGMENTS
                        .iter()
                        .position(|x| {
                            let mut set = HashSet::new();
                            for char in string.chars() {
                                set.insert(configuration[&char]);
                            }
                            *x == set
                        })
                        .unwrap()
                        .to_string()
                })
                .collect::<String>()
                .parse::<usize>()
                .unwrap()
        })
        .sum()
}

#[test]
fn test_sum_output() {
    let entry: Entry =
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
            .parse()
            .unwrap();

    assert_eq!(sum_output(&[entry]), 5353);

    let entries: Vec<Entry> = read_to_string("resources/8test.txt")
        .unwrap()
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    assert_eq!(sum_output(&entries), 61229);
}

pub fn main() {
    let entries: Vec<Entry> = read_to_string("resources/8.txt")
        .unwrap()
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    println!("{}", count_digits(&entries));
    println!("{}", sum_output(&entries));
}
