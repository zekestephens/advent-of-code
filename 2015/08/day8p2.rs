#!/usr/bin/env -S cargo +nightly -Zscript
use std::fs::read;

fn main() {
    let input = read("input.txt").expect("input file could not be read");
    let count2 = input.iter().fold(0, |acc, b| acc + (match b {
            b'"' | b'\\' => 1,
            b'\n' => 2,
            _ => 0
    })) + if let Some(b'\n') = input.last() { 0 } else { 2 };
    println!("{count2}");
}
