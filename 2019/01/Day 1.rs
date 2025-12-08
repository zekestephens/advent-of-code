#!/usr/bin/env rust-script
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

let path = Path::new("input");
let mut file = File::open(&path).unwrap();
let mut s = String::new();
file.read_to_string(&mut s).unwrap();

fn rocket(x: i32) -> i32 {
    let fuel = match x {
        0 => 0,
        _ => x / 3 - 2
    };
    if fuel > 0 { fuel + rocket(fuel) } else {0}
}

println!("{}", s.split("\n").map(str::parse::<i32>).map(Result::unwrap).map(rocket).sum::<i32>())
