#!/usr/bin/env runhaskell
import Control.Monad (when)
import Data.List (elemIndex)
import Data.Set (Set)
import qualified Data.Set as Set
import System.IO (isEOF)

type Position = (Int, Int)

type Grid = [[Bool]]

type Direction = (Int, Int)

directions :: [Direction]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] -- NSEW

startPos :: Position
startPos = (-1, -1) -- invalid pos to default to

parseInput :: [String] -> (Grid, Position)
parseInput lines = (grid, startPos)
  where
    (grid, startPos) = foldl parseLine ([], (-1, -1)) (zip [0 ..] lines)
    parseLine (g, sp) (n, line) =
      let row = map (== '#') (filter (/= '\n') line)
          sp' = case elemIndex '^' line of
            Just idx -> (n, idx)
            Nothing -> sp
       in (g ++ [row], sp')

inBounds :: Position -> Grid -> Bool
inBounds (x, y) g = x >= 0 && x < length g && y >= 0 && y < length (head g)

step :: Grid -> Position -> Int -> Set Position -> (Position, Int, Set Position)
step g pos orient visited =
  let visited' = Set.insert pos visited
      (dx, dy) = directions !! orient
      newPos = (fst pos + dx, snd pos + dy)
   in if inBounds newPos g && g !! fst newPos !! snd newPos
        then (pos, (orient + 1) `mod` 4, visited')
        else (newPos, orient, visited')

explore :: Grid -> Position -> Int -> Set Position -> Set Position
explore g pos orient visited
  | inBounds pos g =
      let (newPos, newOrient, newVisited) = step g pos orient visited
       in explore g newPos newOrient newVisited
  | otherwise = visited

main = do
  input <- readFile "input"
  let (g, startPos) = parseInput (lines input)
      visited = explore g startPos 0 (Set.singleton startPos)
  print (Set.size visited)
