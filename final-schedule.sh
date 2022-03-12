#!/bin/bash

echo "Reproducing final schedule"
echo ""
echo "Modest - exporting to GomX-3.py"
echo ""

rm "Part_2/model/GomX-3.py"
modest export-to-python "Part_2/model/GomX-3.modest" -O "Part_2/model/GomX-3.py"

echo "Running model checker on GomX-3.py"
echo ""
python3 checker.py --s --t --d "Part_2/model/GomX-3.py"