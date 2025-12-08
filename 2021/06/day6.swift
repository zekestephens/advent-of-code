#!/usr/bin/env swift
import Foundation
let inputFile = URL(filePath: "input.txt")
let inputs = try! String(contentsOf: inputFile, encoding: .utf8).trimmingCharacters(in: .newlines)
var l: [Int : Int] = Dictionary(
  inputs
    .split(separator: ",")
    .map { (Int($0)!, 1) },
  uniquingKeysWith: +
)
var up = l  
for iter in 1...256 {
    up[6] = (l[7] ?? 0) + (l[0] ?? 0)
    up[8] = l[0]  
    up[7] = l[8]
    for i in 0...5 {
        up[i] = l[i+1]
    }
    l = up  
    up = l
    if iter == 80 {
        print(l.values.reduce(0, +))
    }
}
print(l.values.reduce(0, +))
