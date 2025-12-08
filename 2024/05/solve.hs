#!/usr/bin/env runhaskell
-- Note: this script assumes input is passed through stdin
import Control.Applicative (many)
import Data.List (partition, sortBy)
import System.IO (isEOF)

-- | (a, b) where a depends on b
type Dependency = (Int, Int)

type Update = [Int]

isSortedBy :: (a -> a -> Ordering) -> [a] -> Bool
isSortedBy cmp = sorted
  where
    sorted [] = True
    sorted [_] = True
    sorted (x : y : xs) = cmp x y /= GT && sorted (y : xs)

main :: IO ()
main = do
  deps <- readDependencies
  updates <- readUpdates
  let middle xs = xs !! (length xs `div` 2)
      depOrder = dependencyOrdering deps
      (sortedUpdates, unsortedUpdates) = partition (isSortedBy depOrder) updates
  print $ sum $ map middle sortedUpdates
  print $ sum $ map (middle . sortBy depOrder) unsortedUpdates

readDependencies :: IO [Dependency]
readDependencies = many $ do
  line <- getLine
  if null line
    then fail "No more input"
    else return $ case break (== '|') line of
      (a, '|' : b) -> (read b, read a)
      _ -> error "Wrong format"

readUpdates :: IO [Update]
readUpdates = many $ do
  eof <- isEOF
  if eof
    then fail "EOF reached"
    else map read . words . map (\c -> if c == ',' then ' ' else c) <$> getLine

dependencyOrdering :: [Dependency] -> Int -> Int -> Ordering
dependencyOrdering deps x y = case (depends x y, depends y x) of
  (True, False) -> GT
  (False, True) -> LT
  _ -> EQ
  where
    depends x y = y `elem` [b | (a, b) <- deps, a == x]
