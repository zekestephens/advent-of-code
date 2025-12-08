#!/usr/bin/env runhaskell
import Data.List

isValid :: [Int] -> Bool
isValid record =
  let pairs = zip record (tail record)
   in (all (uncurry (>)) pairs || all (uncurry (<)) pairs)
        && all (\(x, y) -> let diff = abs (x - y) in diff >= 1 && diff < 4) pairs

isDampenerValid :: [Int] -> Bool
isDampenerValid record = any isValid $ record : [left ++ right | (left, _ : right) <- zip (inits record) (tails record)]

main :: IO ()
main = do
  input <- readFile "input.txt"
  let records = map (map read . words) (lines input)
      validCount = length $ filter isValid records
      dampenerCount = length $ filter isDampenerValid records
  print validCount
  print dampenerCount
