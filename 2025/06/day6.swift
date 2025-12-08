#!/usr/bin/env swift
import Foundation

let space = UInt8(ascii: " ")
let zero = UInt8(ascii: "0")

extension Data.SubSequence {
    var asInt: Int {
        reduce(0) { $0 * 10 + Int($1 - zero) }
    }
}

let inputFile = URL(filePath: "input.txt")

let data = try! Data(contentsOf: inputFile)
let lines = data.split(separator: UInt8(ascii: "\n"))

let opLine = lines.last!
let operations: [(Int, (Int, Int) -> Int)] = opLine
  .split(separator: space)
  .map {
      $0 == [UInt8(ascii: "*")] ? (1, (*)) : (0, (+))
  }

let linum: [[Int]] = lines.dropLast().map { line in
    line.split(separator: space).map(\.asInt)
}

var part1 = linum[0]
  .indices
  .map { i in
      let (initialValue, op) = operations[i]
      return linum.reduce(initialValue) {
          op($0, $1[i])
      }
  }
  .reduce(0, +)

print(part1)

let partitions = opLine
  .enumerated()
  .filter { $1 != space }
  .map(\.offset)


let windows =  zip(partitions, partitions.dropFirst() + [opLine.count]).map(Range.init)

let part2 = zip(operations, windows)
  .map { pair, slice in
      slice
        .compactMap { i in
            let digits = lines
              .dropLast()
              .map { $0[$0.startIndex + i] }
              .filter { $0 != space }
            return digits.isEmpty ? nil : Data(digits).asInt
        }
        .reduce(pair.0, pair.1)
  }
  .reduce(0, +)

print(part2)
