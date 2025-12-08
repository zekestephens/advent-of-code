#!/usr/bin/env runhaskell
{-# LANGUAGE TransformListComp #-}

import Data.List (nub, tails)
import GHC.Exts (groupWith)

type Point = (Int, Int)

parseInput :: String -> [[Point]]
parseInput input =
  [ p
  | (y, line) <- zip [0 ..] $ lines input,
    (x, c) <- zip [0 ..] line,
    c /= '.',
    let p = (x, y),
    then group by
      c
    using
      groupWith
  ]

squaredDistance :: Point -> Point -> Int
squaredDistance (x1, y1) (x2, y2) = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

-- | Determine colinearity of three points based on the area of the triangle formed
colinear :: Point -> Point -> Point -> Bool
colinear (x1, y1) (x2, y2) (x3, y3) = area == 0
  where
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

countAntinodes :: Bool -> Int -> [[Point]] -> Int
countAntinodes part2 dims bands = length $ nub antinodes
  where
    -- Generate all 2-combinations of a list
    pairs band = [(p1, p2) | (p1 : rest) <- tails band, p2 <- rest]
    pointPairs = concatMap pairs bands
    gridPoints = [(x, y) | x <- [0 .. dims - 1], y <- [0 .. dims - 1]]
    -- Check if point p3 satisfies the 1:2 distance requirement
    -- 4 is 2 squared btw
    distanceCriterion p1 p2 p3 =
      (squaredDistance p1 p3 == 4 * squaredDistance p2 p3)
        || (squaredDistance p2 p3 == 4 * squaredDistance p1 p3)
    antinodes =
      [ p3
      | p3 <- gridPoints,
        (p1, p2) <- pointPairs,
        colinear p1 p2 p3,
        part2 || distanceCriterion p1 p2 p3
      ]

main :: IO ()
main = do
  input <- readFile "input"
  let bands = parseInput input
      inputDims = length $ lines input
      partOne = countAntinodes False inputDims bands
      partTwo = countAntinodes True inputDims bands
  print partOne
  print partTwo
