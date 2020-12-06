use itertools::Itertools;
use std::fs::read_to_string;

fn parse_passes() -> Vec<String> {
    read_to_string("resources/5.txt")
        .unwrap()
        .lines()
        .map(str::to_string)
        .collect()
}

fn u8_from_binary_str(binary_str: &str) -> u8 {
    u8::from_str_radix(binary_str, 2).unwrap()
}

fn row(pass: &str) -> u8 {
    u8_from_binary_str(pass[..7].replace("F", "0").replace("B", "1").as_str())
}

fn column(pass: &str) -> u8 {
    u8_from_binary_str(pass[7..].replace("L", "0").replace("R", "1").as_str())
}

fn seat_id(pass: &str) -> u16 {
    row(pass) as u16 * 8 + column(pass) as u16
}

fn highest_seat_id(passes: &[String]) -> u16 {
    passes
        .iter()
        .map(String::as_str)
        .map(seat_id)
        .max()
        .unwrap()
}

fn missing_seat_id(passes: &[String]) -> u16 {
    let seat_ids: Vec<u16> = passes
        .iter()
        .map(String::as_str)
        .map(seat_id)
        .sorted()
        .collect();
    let (_, index_after_missing) = seat_ids
        .iter()
        .enumerate()
        .find(|(index, seat_id)| (*seat_id - seat_ids[0]) as usize != *index)
        .unwrap();
    index_after_missing - 1
}

pub fn main() {
    let passes = parse_passes();
    println!("{}", highest_seat_id(&passes));
    println!("{}", missing_seat_id(&passes));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_row() {
        assert_eq!(row("BFFFBBFRRR"), 70);
        assert_eq!(row("FFFBBBFRRR"), 14);
        assert_eq!(row("BBFFBBFRLL"), 102);
    }

    #[test]
    fn test_column() {
        assert_eq!(column("BFFFBBFRRR"), 7);
        assert_eq!(column("FFFBBBFRRR"), 7);
        assert_eq!(column("BBFFBBFRLL"), 4);
    }

    #[test]
    fn test_seat_id() {
        assert_eq!(seat_id("BFFFBBFRRR"), 567);
        assert_eq!(seat_id("FFFBBBFRRR"), 119);
        assert_eq!(seat_id("BBFFBBFRLL"), 820);
    }
}
