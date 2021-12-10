use either::*;
use std::fs::read_to_string;

#[derive(Debug, PartialEq)]
enum Bracket {
    Round,
    Square,
    Curly,
    Angle,
}

#[derive(Debug, PartialEq)]
enum BracketError {
    Corrupted(Bracket),
    Incomplete(Vec<Bracket>),
}

#[cfg(test)]
fn tokenize_brackets(s: &str) -> Vec<Bracket> {
    s.chars()
        .map(|c| match c {
            '(' => Bracket::Round,
            '[' => Bracket::Square,
            '{' => Bracket::Curly,
            '<' => Bracket::Angle,
            ')' => Bracket::Round,
            ']' => Bracket::Square,
            '}' => Bracket::Curly,
            '>' => Bracket::Angle,
            _ => unreachable!(),
        })
        .collect()
}

fn tokenize_eithers(s: &str) -> Vec<Either<Bracket, Bracket>> {
    s.chars()
        .map(|c| match c {
            '(' => Left(Bracket::Round),
            '[' => Left(Bracket::Square),
            '{' => Left(Bracket::Curly),
            '<' => Left(Bracket::Angle),
            ')' => Right(Bracket::Round),
            ']' => Right(Bracket::Square),
            '}' => Right(Bracket::Curly),
            '>' => Right(Bracket::Angle),
            _ => unreachable!(),
        })
        .collect()
}

#[cfg(test)]
lazy_static! {
    static ref TEST_STR: &'static str = "[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]";
}

fn check_brackets(s: &str) -> Result<(), BracketError> {
    let mut stack = Vec::new();
    for token in tokenize_eithers(s) {
        match token {
            Left(bracket) => stack.push(bracket),
            Right(bracket) => match stack.pop() {
                Some(top) => {
                    if bracket != top {
                        return Err(BracketError::Corrupted(bracket));
                    }
                }
                None => return Err(BracketError::Corrupted(bracket)),
            },
        }
    }
    if stack.is_empty() {
        Ok(())
    } else {
        stack.reverse();
        Err(BracketError::Incomplete(stack))
    }
}

#[test]
fn test_check_brackets() {
    assert_eq!(
        check_brackets("[({(<(())[]>[[{[]{<()<>>"),
        Err(BracketError::Incomplete(tokenize_brackets("}}]])})]")))
    );
    assert_eq!(
        check_brackets("[(()[<>])]({[<{<<[]>>("),
        Err(BracketError::Incomplete(tokenize_brackets(")}>]})")))
    );
    assert_eq!(
        check_brackets("{([(<{}[<>[]}>{[]{[(<()>"),
        Err(BracketError::Corrupted(Bracket::Curly))
    );
    assert_eq!(
        check_brackets("(((({<>}<{<{<>}{[]{[]{}"),
        Err(BracketError::Incomplete(tokenize_brackets("}}>}>))))")))
    );
    assert_eq!(
        check_brackets("[[<[([]))<([[{}[[()]]]"),
        Err(BracketError::Corrupted(Bracket::Round))
    );
    assert_eq!(
        check_brackets("[{[{({}]{}}([{[{{{}}([]"),
        Err(BracketError::Corrupted(Bracket::Square))
    );
    assert_eq!(
        check_brackets("{<[[]]>}<{[{[{[]{()[[[]"),
        Err(BracketError::Incomplete(tokenize_brackets("]]}}]}]}>")))
    );
    assert_eq!(
        check_brackets("[<(<(<(<{}))><([]([]()"),
        Err(BracketError::Corrupted(Bracket::Round)),
    );
    assert_eq!(
        check_brackets("<{([([[(<>()){}]>(<<{{"),
        Err(BracketError::Corrupted(Bracket::Angle))
    );
    assert_eq!(
        check_brackets("<{([{{}}[<[[[<>{}]]]>[]]"),
        Err(BracketError::Incomplete(tokenize_brackets("])}>")))
    );
}

fn corrupted_bracket_score(s: &str) -> u32 {
    s.lines()
        .map(|line| match check_brackets(line) {
            Err(BracketError::Corrupted(Bracket::Round)) => 3,
            Err(BracketError::Corrupted(Bracket::Square)) => 57,
            Err(BracketError::Corrupted(Bracket::Curly)) => 1197,
            Err(BracketError::Corrupted(Bracket::Angle)) => 25137,
            _ => 0,
        })
        .sum()
}

#[test]
fn test_corrupted_bracket_score() {
    assert_eq!(corrupted_bracket_score(&TEST_STR), 26397);
}

fn incomplete_bracket_score(s: &str) -> u64 {
    let mut scores: Vec<u64> = s
        .lines()
        .filter_map(|line| match check_brackets(line) {
            Err(BracketError::Incomplete(stack)) => Some(stack.iter().fold(0, |acc, x| {
                acc * 5
                    + match x {
                        Bracket::Round => 1,
                        Bracket::Square => 2,
                        Bracket::Curly => 3,
                        Bracket::Angle => 4,
                    }
            })),
            _ => None,
        })
        .collect();
    scores.sort_unstable();
    scores[scores.len() / 2]
}

#[test]
fn test_incomplete_bracket_score() {
    assert_eq!(incomplete_bracket_score(&TEST_STR), 288957);
}

pub fn main() {
    let s = read_to_string("resources/10.txt").unwrap();
    println!("{}", corrupted_bracket_score(&s));
    println!("{}", incomplete_bracket_score(&s));
}
