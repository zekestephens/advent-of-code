#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
;;;; Still a work in progress as you can see
(require 'cl-lib)
(with-temp-buffer
  (insert-file-contents "sample.txt")
  (goto-char (point-min))
  (let ((locations nil))
    (cl-loop
     for line = (string-trim (thing-at-point 'line))
     for i from 0
     do (cl-loop for c across line
                 for j from 0
                 when (char-equal c ?\@)
                 do (push (cons i j) locations))
     do (forward-line 1)
     until (eobp))
    (message "%s" locations)))
