#!/usr/bin/env bb
(import 'java.io.BufferedReader 'java.io.FileReader)
(require '[clojure.string :as str])

(let [input-lines (line-seq (BufferedReader. (FileReader. "input.txt")))
      [lefts rights] (->> input-lines
                          (map #(str/split % #"\s+"))
                          (map (fn [[l r]] [(Integer/parseInt l) (Integer/parseInt r)]))
                          (apply map vector))
      sorted-lefts (sort lefts)
      sorted-rights (sort rights)]

  (println (->> (map - sorted-lefts sorted-rights)
                (map #(Math/abs %))
                (reduce +)))
  (println (->> sorted-lefts
                (map #(* % (get (frequencies sorted-rights) %)))
                (reduce +))))
