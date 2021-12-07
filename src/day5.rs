use std::{
    cmp::PartialEq, fmt, fs::read_to_string, num::ParseIntError, result::Result, str::FromStr,
};

#[derive(Clone, Debug, PartialEq)]
struct Point {
    x: u16,
    y: u16,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{},{}", self.x, self.y)
    }
}

#[derive(Debug, PartialEq)]
enum ParsePointError {
    ParseIntError(ParseIntError),
    NoDelimiterError,
}

impl FromStr for Point {
    type Err = ParsePointError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (x, y) = s.split_once(',').ok_or(Self::Err::NoDelimiterError)?;

        Ok(Self {
            x: x.parse().map_err(Self::Err::ParseIntError)?,
            y: y.parse().map_err(Self::Err::ParseIntError)?,
        })
    }
}

#[test]
fn point_from_str() {
    assert_eq!("1,2".parse::<Point>(), Ok(Point { x: 1, y: 2 }));
    assert!(matches!(
        "1.0,2.0".parse::<Point>(),
        Err(ParsePointError::ParseIntError(_))
    ));
    assert_eq!("1".parse::<Point>(), Err(ParsePointError::NoDelimiterError));
}

#[test]
fn point_display() {
    assert_eq!(Point { x: 1, y: 2 }.to_string(), "1,2");
}

#[derive(Clone, Debug, PartialEq)]
struct Line {
    point_1: Point,
    point_2: Point,
}

impl Line {
    fn is_horizontal(&self) -> bool {
        self.point_1.y == self.point_2.y
    }

    fn is_vertical(&self) -> bool {
        self.point_1.x == self.point_2.x
    }

    fn is_straight(&self) -> bool {
        self.is_horizontal() || self.is_vertical()
    }
}

impl fmt::Display for Line {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} -> {}", self.point_1, self.point_2)
    }
}

#[test]
fn line_display() {
    assert_eq!(
        Line {
            point_1: Point { x: 1, y: 2 },
            point_2: Point { x: 3, y: 4 },
        }
        .to_string(),
        "1,2 -> 3,4",
    );
}

#[derive(Debug, PartialEq)]
enum ParseLineError {
    ParsePointError(ParsePointError),
    NoDelimiterError,
}

impl FromStr for Line {
    type Err = ParseLineError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (point_1, point_2) = s.split_once(" -> ").ok_or(Self::Err::NoDelimiterError)?;

        Ok(Self {
            point_1: point_1.parse().map_err(Self::Err::ParsePointError)?,
            point_2: point_2.parse().map_err(Self::Err::ParsePointError)?,
        })
    }
}

#[test]
fn line_from_str() {
    assert_eq!(
        "1,2 -> 3,4".parse::<Line>(),
        Ok(Line {
            point_1: Point { x: 1, y: 2 },
            point_2: Point { x: 3, y: 4 },
        })
    );
    assert_eq!("1,2".parse::<Line>(), Err(ParseLineError::NoDelimiterError));
}

struct Diagram(Vec<Vec<u8>>);

fn range_between(left: u16, right: u16) -> Box<dyn Iterator<Item = u16>> {
    if left < right {
        Box::new(left..=right)
    } else {
        Box::new((right..=left).rev())
    }
}

impl Diagram {
    fn new(lines: &[Line]) -> Self {
        let width = match lines
            .iter()
            .flat_map(|line| [line.point_1.x, line.point_2.x])
            .max()
        {
            Some(n) => n + 1,
            None => 0,
        };

        let height = match lines
            .iter()
            .flat_map(|line| [line.point_1.y, line.point_2.y])
            .max()
        {
            Some(n) => n + 1,
            None => 0,
        };

        let grid = vec![vec![0; width as usize]; height as usize];

        let mut result = Self { 0: grid };

        for line in lines {
            result.set_line(line);
        }

        result
    }

    fn count_overlaps(&self) -> u16 {
        self.0
            .iter()
            .map(|row| row.iter().filter(|&&x| x > 1).count() as u16)
            .sum()
    }

    fn set_point(&mut self, point: &Point) {
        self.0[point.y as usize][point.x as usize] += 1;
    }

    fn set_line(&mut self, line: &Line) {
        let points: Box<dyn Iterator<Item = Point>> = if line.is_horizontal() {
            Box::new(
                range_between(line.point_1.x, line.point_2.x).map(|x| Point {
                    x,
                    y: line.point_1.y,
                }),
            )
        } else if line.is_vertical() {
            Box::new(
                range_between(line.point_1.y, line.point_2.y).map(|y| Point {
                    x: line.point_1.x,
                    y,
                }),
            )
        } else {
            Box::new(
                range_between(line.point_1.x, line.point_2.x)
                    .zip(range_between(line.point_1.y, line.point_2.y))
                    .map(|(x, y)| Point { x, y }),
            )
        };

        for point in points {
            self.set_point(&point);
        }
    }
}

#[test]
fn test_diagram() {
    let lines: Vec<Line> = "0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"
        .lines()
        .map(|line| line.parse::<Line>().unwrap())
        .collect();
    let straight_lines: Vec<Line> = lines
        .iter()
        .cloned()
        .filter(|line| line.is_straight())
        .collect();

    let diagram_1 = Diagram::new(&straight_lines);
    assert_eq!(
        diagram_1.to_string(),
        ".......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111...."
    );
    assert_eq!(diagram_1.count_overlaps(), 5);

    let diagram_2 = Diagram::new(&lines);
    assert_eq!(
        diagram_2.to_string(),
        "1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."
    );
    assert_eq!(diagram_2.count_overlaps(), 12);
}

impl fmt::Display for Diagram {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut it = self.0.iter().peekable();
        while let Some(row) = it.next() {
            for cell in row {
                if *cell == 0 {
                    write!(f, ".")?;
                } else {
                    write!(f, "{}", cell)?;
                }
            }
            if it.peek().is_some() {
                writeln!(f)?;
            }
        }
        Ok(())
    }
}

pub fn main() {
    let lines: Vec<Line> = read_to_string("resources/5.txt")
        .unwrap()
        .lines()
        .map(|line| line.parse::<Line>().unwrap())
        .collect();
    let straight_lines: Vec<Line> = lines
        .iter()
        .cloned()
        .filter(|line| line.is_straight())
        .collect();

    println!("{}", Diagram::new(&straight_lines).count_overlaps());
    println!("{}", Diagram::new(&lines).count_overlaps());
}
