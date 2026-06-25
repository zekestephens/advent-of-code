#!/usr/bin/env -S cargo +nightly -Zscript
use std::fs;
use std::collections::HashMap;

fn nicep1(&candidate: &&[u8]) -> bool {
    // 3 conditions:
    // 1. vowel count (aeiou) > 2
    // 2. double letter (must remember last letter
    // 3. does NOT contain ab, cd, pq, or xy
    let mut count_vowel = 0;
    let mut has_double_letter = false;
    let mut has_forbidden_pair = false;
    let mut last_letter = 0u8;
    for &letter in candidate {
        if b"aeiou".contains(&letter) {
            count_vowel += 1;
        }
        if letter == last_letter {
            has_double_letter = true;
        } else if let b"ab" | b"cd" | b"pq" | b"xy" = &[last_letter, letter] {
            has_forbidden_pair = true
        }
        last_letter = letter;
    }
    count_vowel > 2 && !has_forbidden_pair && has_double_letter
}

fn nicep2(candidate: &&[u8]) -> bool {
    // Must contain a repeated pair.
    let mut pairs = HashMap::new(); // Keep track of all pairs seen before
    let mut two_pair = false;
    // Can't take slices on empty arrays
    if candidate.len() < 1 { return false; }
    for i in 0..(candidate.len() - 1) {
        let pair = [candidate[i], candidate[i+1]];
        // pairs can't overlap
        if let Some(&idx) = pairs.get(&pair) && idx < i - 1 {
            two_pair = true;
            break;
        }
        pairs.entry(pair).or_insert(i);
    }
    return two_pair && candidate.array_windows().any(|&[a, _, c]| a == c);
}

fn main() {
    let data = fs::read("input.txt").expect("File input.txt could not be read");
    let lines = data.split(|&c| c == b'\n');
    let count1 = lines.clone().filter(nicep1).count();
    let count2 = lines.filter(nicep2).count();
    println!("{count1}, {count2}")
}
