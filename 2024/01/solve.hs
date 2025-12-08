#!/usr/bin/env runhaskell
import System.IO
import Data.List

main = do
    contents <- readFile "input.txt"
    let pairs = map ((\[l, r] -> (read l :: Int, read r :: Int)) . words) $ lines contents
        lefts = sort $ map fst pairs
        rights = sort $ map snd pairs

        -- First sum: absolute differences
        diffSum = sum $ zipWith (\x y -> abs (x - y)) lefts rights

        -- Second sum: product of left values with their counts in rights
        countSum = sum [x * length (filter (== x) rights) | x <- lefts]

    print diffSum
    print countSum
