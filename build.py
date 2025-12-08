#!/usr/bin/env python3
"""
Simple task runner for Advent of Code problems.

Usage: ./build.py 2025/07
"""
import argparse
from pathlib import Path
from stat import S_IXUSR
from subprocess import run

parser = argparse.ArgumentParser()
parser.add_argument("path", help="directory to execute scripts in", type=Path)
args = parser.parse_args()

for script in args.path.iterdir():
    mode = script.stat().st_mode
    if script.is_file() and mode & S_IXUSR:
        print(f'Running {script}...')
        run(script.resolve(), cwd=args.path)
