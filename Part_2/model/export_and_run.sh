#!/bin/zsh

echo "FILENAME: $1"
echo ""
echo "Modest - exporting to $1.py"
echo ""

rm "$1".py
modest export-to-python "$1".modest -O "$1".py
python3 ../../Part\ 1/checker.py --d --s --t "$1".py