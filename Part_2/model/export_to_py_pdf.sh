#!/bin/zsh

echo "FILENAME: $1"
echo ""
echo "Modest - exporting to $1.pdf and $1.py"
echo ""

rm "$1".dot
rm "$1".py
modest export-to-dot "$1".modest -O "$1".dot --dot pdf "$1".pdf --open-output
modest export-to-python "$1".modest -O "$1".py
