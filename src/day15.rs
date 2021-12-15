use std::{
    cmp::Ordering, collections::BinaryHeap, convert::Infallible, fs::read_to_string, str::FromStr,
};

fn rotate(x: u8, rotations: u8) -> u8 {
    let y = x + rotations;
    y % 10 + y / 10
}

#[test]
fn test_rotate() {
    assert_eq!(rotate(1, 0), 1);

    assert_eq!(rotate(1, 1), 2);
    assert_eq!(rotate(2, 1), 3);
    assert_eq!(rotate(3, 1), 4);
    assert_eq!(rotate(4, 1), 5);
    assert_eq!(rotate(5, 1), 6);
    assert_eq!(rotate(6, 1), 7);
    assert_eq!(rotate(7, 1), 8);
    assert_eq!(rotate(8, 1), 9);
    assert_eq!(rotate(9, 1), 1);

    /*
    8 9 1 2 3
    9 1 2 3 4
    1 2 3 4 5
    2 3 4 5 6
    3 4 5 6 7
     */

    assert_eq!(rotate(8, 1), 9);
    assert_eq!(rotate(8, 2), 1);
    assert_eq!(rotate(8, 3), 2);
    assert_eq!(rotate(8, 4), 3);
    assert_eq!(rotate(8, 5), 4);
    assert_eq!(rotate(8, 6), 5);
    assert_eq!(rotate(8, 7), 6);
    assert_eq!(rotate(8, 8), 7);
}

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
struct Point {
    x: usize,
    y: usize,
}

#[derive(Eq, PartialEq)]
struct State {
    cost: u16,
    point: Point,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

#[derive(Debug, PartialEq)]
struct Cave(Vec<Vec<u8>>);

impl Cave {
    fn risk(&self) -> u16 {
        let mut q = BinaryHeap::new();

        let mut dist = vec![vec![u16::MAX; self.0[0].len()]; self.0.len()];
        dist[0][0] = 0;

        let target = Point {
            x: self.0[0].len() - 1,
            y: self.0.len() - 1,
        };

        q.push(State {
            cost: 0,
            point: Point { x: 0, y: 0 },
        });

        while let Some(State { cost, point }) = q.pop() {
            if point == target {
                return cost;
            }

            let above = (point.y > 0).then(|| Point {
                x: point.x,
                y: point.y - 1,
            });
            let below = (point.y + 1 < self.0.len()).then(|| Point {
                x: point.x,
                y: point.y + 1,
            });
            let left = (point.x > 0).then(|| Point {
                x: point.x - 1,
                y: point.y,
            });
            let right = (point.x + 1 < self.0[point.y].len()).then(|| Point {
                x: point.x + 1,
                y: point.y,
            });

            for v in [above, below, left, right].iter().flatten() {
                let cost = cost + self.0[v.y][v.x] as u16;
                if cost < dist[v.y][v.x] {
                    q.push(State { cost, point: *v });
                    dist[v.y][v.x] = cost;
                }
            }
        }

        unreachable!();
    }

    fn expand(&self) -> Cave {
        let width = self.0[0].len();
        let height = self.0.len();
        let mut cave = Cave(vec![vec![0; width * 5]; height * 5]);
        for y in 0..(height * 5) {
            for x in 0..(width * 5) {
                cave.0[y][x] = rotate(
                    self.0[y % height][x % width],
                    (x / width + y / height) as u8,
                );
            }
        }
        cave
    }
}

impl FromStr for Cave {
    type Err = Infallible;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Self(
            s.lines()
                .map(|line| {
                    line.chars()
                        .map(|char| char.to_digit(10).unwrap() as u8)
                        .collect()
                })
                .collect(),
        ))
    }
}

#[test]
fn test_risk() {
    let cave: Cave = "1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"
        .parse()
        .unwrap();
    assert_eq!(cave.risk(), 40);
    assert_eq!(cave.expand().risk(), 315);
}

#[test]
fn test_expand() {
    let cave = Cave(vec![vec![8]]);
    let new_cave: Cave = "89123
91234
12345
23456
34567"
        .parse()
        .unwrap();
    assert_eq!(cave.expand(), new_cave);
}

pub fn main() {
    let cave: Cave = read_to_string("resources/15.txt").unwrap().parse().unwrap();

    println!("{}", cave.risk());
    println!("{}", cave.expand().risk());
}
