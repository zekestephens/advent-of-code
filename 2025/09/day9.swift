#!/usr/bin/env swift
// had to take some deep inspiration from this other solution
// https://github.com/jameswrw/AoC-2025/blob/main/Advent%202025/Advent9.swift
//
// my initial approach in python was inadequate, so I went with CoreGraphics as
// it seemed pretty straightforward.
//
// the other main approach people went with was coordinate compression, which I
// will have to try if I have time
import Foundation
import CoreGraphics

let inputFile = URL(filePath: "input.txt")
let inputs = try! String(contentsOf: inputFile, encoding: .utf8)
var corners = inputs.split(separator: "\n").map { line in
    let xy = line.split(separator: ",").map { Int($0)! }
    return CGPoint(x: xy[0], y: xy[1])
}
let border = CGMutablePath()

border.move(to: corners.first!)
for point in corners.dropFirst() {
    border.addLine(to: point)
}
border.closeSubpath()
var maxArea: CGFloat = 0
for i in 0..<corners.count-1 {
    for j in i+1..<corners.count {
        let rect = CGRect(
          origin: corners[i],
          size: CGSize(
            width: corners[j].x - corners[i].x,
            height: corners[j].y - corners[i].y
          )
        )
        let path = CGPath(
          rect: rect,
          transform: nil
        )

        let intersection = border.intersection(path)

        var intersectionRect = CGRect.zero
        intersection.isRect(&intersectionRect)
                
        let epsilon = 1e-6
        if abs(intersectionRect.width - rect.width) < epsilon &&
             abs(intersectionRect.height - rect.height) < epsilon {
            let w = abs(corners[i].x - corners[j].x)
            let h = abs(corners[i].y - corners[j].y)
            maxArea = max(maxArea, (w + 1) * (h + 1))
        }
    }
}
print(Int(maxArea))
