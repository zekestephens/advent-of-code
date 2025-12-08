#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
;; Day 2
(require 'cl-lib)
(defun invalid1 (num)
  (let* ((s (number-to-string num))
         (len (length s)))
    (if (string-equal
         (substring s 0 (/ len 2))
         (substring s (/ len 2)))
        num 0)))

(defun invalid2 (num)
  (let* ((s (number-to-string num))
         (len (length s)))
    (cl-loop for l from 1 to (/ len 2)
             for sub = (seq-take s l)
             for ax = (apply #'concat (make-list (/ len l) sub))
             when (string-equal s ax)
             return t)))

(defun sum-invalid (total1 total2 ranges)
  (if (null ranges)
      (list total1 total2)
    (sum-invalid
     (+ total1
        (cl-loop for i from (car ranges) to (cadr ranges)
                 sum (invalid1 i)))
     (+ total2
        (cl-loop for i from (car ranges) to (cadr ranges)
                 sum (if (invalid2 i) i 0)))
     (cddr ranges))))


(with-temp-buffer
  (insert-file-contents "input.txt")
  (cl-destructuring-bind (part1 part2)
      (sum-invalid
       0
       0
       (mapcar
        #'string-to-number
        (split-string (thing-at-point 'line) "[,-]")))
    (message "%i %i" part1 part2)))
