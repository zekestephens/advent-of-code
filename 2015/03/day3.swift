#!/usr/bin/env swift
import Foundation

struct Point: Hashable {
    var x: Int
    var y: Int

    static func == (lhs: Point, rhs: Point) -> Bool {
        return lhs.x == rhs.x && lhs.y == rhs.y
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(x)
        hasher.combine(y)
    }
}

let content = try String(contentsOf: URL(fileURLWithPath: "input.txt"), encoding: .utf8)
var position = Point(x: 0, y: 0)
var part2 = [Point(x: 0, y: 0), Point(x: 0, y: 0)]

var houses1: Set = [position]
var houses2: Set = [part2[0]]

for (i, c) in content.enumerated() {
    switch c {
    case "^":
        position.y -= 1
        part2[i % 2].y -= 1
    case "v":
        position.y += 1
        part2[i % 2].y += 1
    case "<":
        position.x -= 1
        part2[i % 2].x -= 1
    case ">":
        position.x += 1
        part2[i % 2].x += 1
    default:
        _ = 69
    }
    houses1.insert(position)
    houses2.insert(part2[i % 2])
}


print(houses1.count)
print(houses2.count)
