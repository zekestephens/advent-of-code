#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
(require 'cl-lib)
(defun joltage (bank limit)
  (string-to-number
   (apply #'string
          (cl-loop with offset = 0
                   with n = (length bank)
                   for stop from (1- limit) downto 0
                   for slice = (substring bank offset (- n stop))
                   for (elem idx) = (maxdex slice)
                   do (setf offset (+ offset 1 idx))
                   collect elem))))

(defun maxdex (se)
  (let ((max-elem (elt se 0))
        (max-idx 0))
    (dotimes (i (length se))
      (when (> (elt se i) max-elem)
        (setf max-elem (elt se i))
        (setf max-idx i)))
    (list max-elem max-idx)))

(with-temp-buffer
  (insert-file-contents "input.txt")
  (goto-char (point-min))
  (let ((sum1 0)
        (sum2 0))
    (while (not (eobp))
      (let ((line (string-trim (thing-at-point 'line))))
        (setf sum1 (+ sum1 (joltage line 2)))
        (setf sum2 (+ sum2 (joltage line 12))))
      (forward-line 1))
    (message "%d %d" sum1 sum2)))
