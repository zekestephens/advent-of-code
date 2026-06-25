#!/usr/bin/env -S cargo +nightly -Zscript

fn looksay(num: &[u8]) -> Vec<u8> {
    let mut res = vec![];
    let mut current_digit = None;
    let mut current_count = 0;
    for i in num {
        if current_digit == Some(i) {
            current_count += 1;
        } else {
            if let Some(&d) = current_digit {
                for cd in current_count.to_string().bytes() {
                    res.push(cd);
                }
                res.push(d);
            }
            current_count = 1;
            current_digit = Some(i);
        }
    }
    if let Some(&d) = current_digit {
        for cd in current_count.to_string().bytes() {
            res.push(cd);
        }
        res.push(d);
    }
    res
}

fn main() {
    let iput = include_bytes!("input");
    let mut rec_iput: Vec<u8> = iput.iter().map(|&x| x).collect();
    for _ in 1..=40 {
        rec_iput = looksay(&rec_iput);
    }
    // Part 1
    println!("{}", rec_iput.len());
    for _ in 1..=10 {
        rec_iput = looksay(&rec_iput);
    }
    // Part 2
    println!("{}", rec_iput.len());
}
