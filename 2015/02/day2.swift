#!/usr/bin/env swift
import Foundation

let inputFile = URL(filePath: "input")
let input = try! String(contentsOf: inputFile, encoding: .utf8)
let lines = input.split(separator: "\n")

var totalPaper = 0
var totalRibbon = 0
for line in lines {
    let dims = line.split(separator: "x").map { Int($0)! }.sorted()
    let l = dims[0]
    let w = dims[1]
    let h = dims[2]
    let sides = [l*w, w*h, h*l].sorted()
    totalRibbon += 2 * (l + w) + l * h * w
    totalPaper +=  sides[0] + 2 * sides.reduce(0) { $0 + $1 }
}
print(totalPaper)
print(totalRibbon)
