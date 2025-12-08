#!/usr/bin/env emacs --script
;; -*- lexical-binding: t; -*-
;; Work in progress
(with-temp-buffer
  (insert-file-contents "input")
  (goto-char (point-min))
  (while (re-search-forward
          (rx (group (+ digit)) "x"
              (group (+ digit)) "x"
              (group (+ digit)))
          nil t)
    (replace-match "\\1"))
  (goto-char (point-min))
  (thing-at-point 'line))
