#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
(require 'cl-lib)
(princ
 ;; Part 1
 (format "%s\n%s\n"
         (with-temp-buffer
           (insert-file-contents "input")
           (cl-loop initially (goto-char (point-min))
                    for i from 1
                    for c = (following-char)
                    until (= c 0)
                    do (forward-char)
                    sum (if (= c ?\() 1 -1)))


         ;; Part 2
         (with-temp-buffer
           (insert-file-contents "input")
           (cl-loop initially (goto-char (point-min))
                    with floor = 0
                    for i from 1
                    for c = (following-char)
                    until (= c 0)
                    do (forward-char)
                    do (if (= c ?\() (incf floor) (decf floor))
                    when (< floor 0)
                    return i))))
