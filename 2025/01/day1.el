#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
;; Day 1
(require 'cl-lib)
(with-temp-buffer
  (insert-file-contents "input.txt")
  (goto-char (point-min))
  (let ((pos 50)
        (count1 0)
        (count2 0))
    (while (re-search-forward
            (rx (group (| "L" "R"))
                (group (+ digit)))
            nil t)
      (let ((d (if (string-equal (match-string 1) "L") -1 1))
            (n (string-to-number (match-string 2))))
        (cl-loop repeat n
                 do (setf pos (mod (+ pos d) 100))
                 when (= pos 0)
                 do (incf count2))
        (when (= pos 0) (incf count1))))
    (message "%i %i" count1 count2)))
