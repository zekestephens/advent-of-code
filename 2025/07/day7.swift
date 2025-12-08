#!/usr/bin/env swift
import Foundation

let inputFile = URL(filePath: "input.txt")

let data = try! Data(contentsOf: inputFile)
let lines = data.split(separator: UInt8(ascii: "\n"))

let splitters = lines.dropFirst().map { line in
    line.map { $0 == UInt8(ascii: "^") }
}

var split = 0
var beamCounts = lines.first!.map { $0 == UInt8(ascii: "S") ? 1 : 0 }

for row in splitters {
    for i in row.indices where row[i] && beamCounts[i] > 0 {
        split += 1
        beamCounts[i - 1] += beamCounts[i]
        beamCounts[i + 1] += beamCounts[i]
        beamCounts[i] = 0
    }
}

print(split)
print(beamCounts.reduce(0, +))
