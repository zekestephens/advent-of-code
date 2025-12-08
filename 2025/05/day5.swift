#!/usr/bin/env swift
// work in progress
import Foundation

let contents = try String(
  contentsOf: URL(fileURLWithPath: "sample.txt"),
  encoding: .utf8,
)

contents.split(separator: "\n")
print(contents)
