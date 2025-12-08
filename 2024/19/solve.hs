#!/usr/bin/env runhaskell
{-# LANGUAGE BangPatterns #-}

import Control.DeepSeq (force)
import Data.Array (Array, array, (!))
import qualified Data.ByteString.Char8 as B
import Data.List (foldl')

type Pattern = B.ByteString

type Input = B.ByteString

-- Dynamic programming approach
countMatches :: [Pattern] -> Input -> Int
countMatches patterns input = dp ! n
  where
    n = B.length input
    dp = array (0, n) $ (0, 1) : [(i, ways i) | i <- [1 .. n]]

    ways :: Int -> Int
    ways i = sum [if matchAtPos p i then dp ! (i - B.length p) else 0 | p <- patterns]

    matchAtPos :: Pattern -> Int -> Bool
    matchAtPos p i
      | B.length p > i = False
      | otherwise = B.isPrefixOf p (B.drop (i - B.length p) input)

main :: IO ()
main = do
  input <- B.readFile "input"
  let (patternsLine : _ : cases) = B.lines input
      !patterns = force $ map B.strip $ B.split ',' patternsLine
      -- Pre-verify patterns are non-empty to avoid edge cases
      !validPatterns = filter (not . B.null) patterns
      !totalValidParses = foldl' (\acc s -> acc + countMatches validPatterns s) 0 cases
  print totalValidParses
