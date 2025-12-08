#!/usr/bin/env cabal
{- cabal:
build-depends: base, regex-tdfa
-}
import Data.List
import Text.Regex.TDFA

-- Helper function to evaluate mul expressions
evalMul :: String -> Int
evalMul str =
  let matches = getAllTextMatches (str =~ "[0-9]+" :: AllTextMatches [] String)
      nums = take 2 $ map read matches
   in case nums of
        [a, b] -> a * b
        _ -> 0

-- Get valid sections (between do's and don'ts)
getValidSections :: [String] -> [String]
getValidSections [] = []
getValidSections xs = case break (== "don't()") xs of
  (valid, []) -> valid
  (valid, _ : rest) -> valid ++ getValidSections (dropWhile (/= "do()") rest)

main :: IO ()
main = do
  contents <- readFile "input"

  -- First part: sum of all mul expressions
  let mulExpressions = getAllTextMatches (contents =~ "mul\\([0-9]+,[0-9]+\\)" :: AllTextMatches [] String)
  let sum1 = sum $ map evalMul mulExpressions
  print sum1

  -- Second part: process valid sections
  let allExpressions = getAllTextMatches (contents =~ "mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)" :: AllTextMatches [] String)
  let validMuls = filter (isPrefixOf "mul") $ getValidSections allExpressions
  print $ sum $ map evalMul validMuls
