#!/usr/bin/env runhaskell
{-# LANGUAGE BangPatterns #-}

import Control.Monad (replicateM)
import Data.List

lineParse :: String -> (Int, [Int])
lineParse s = case words s of
  (x : xs) -> (read (init x), read <$> xs)
  _ -> error "Invalid input"

concatenate :: Int -> Int -> Int
concatenate x y = x * (10 ^ length (show y)) + y

calibrationResult :: [Int -> Int -> Int] -> [(Int, [Int])] -> Int
calibrationResult ops dat = sum $ fst <$> filter checkTarget dat
  where
    checkTarget (target, nums) = elem target $ evaluate nums <$> replicateM (length nums - 1) ops
    evaluate (x : xs) operatorList = foldl' (\acc (op, n) -> op acc n) x (zip operatorList xs)
    evaluate [] _ = error "Empty number list"

main :: IO ()
main = do
  input <- readFile "input"
  let dat = lineParse <$> lines input
      !partOne = calibrationResult [(+), (*)] dat
      !partTwo = calibrationResult [(+), (*), concatenate] dat
  print partOne
  print partTwo
