#!/usr/bin/env -S cargo +nightly -Zscript
---cargo
[dependencies]
anyhow = "1"
fs-err = "3"
---
use anyhow::Result;
use std::io::prelude::*;
use fs_err::File;

fn main() -> Result<()> {
    let mut fh = File::open("input.txt")?;
    let mut buf = [0u8];
    let mut count1 = 0;
    while let Ok(1) = fh.read(&mut buf) {
        count1 += match &buf[..] {
            b"\"" => 1,
            b"\\" => {
                fh.read(&mut buf)?;
                match &buf[..] {
                    b"x" => {
                        fh.read(&mut buf)?;
                        fh.read(&mut buf)?;
                        3
                    },
                    b"\\" | b"\"" => 1,
                    _ => 0
                }
            },
            _ => 0
        };
    }
    println!("{count1}");
    Ok(())
}
