# CSV to arrays converter
This folder contains the GomX-3 nanosattelite data and a Python script [convertdata.py](convertdata.py) to convert this CSV data to transient arrays and array index sizes that can be used in the GomX-3 Modest model. 

After executing the script:
```shellscript
python3 convertdata.py
```
A file called [data.txt](data.txt) is created that contains the data that can be copied and pasted into [GomX-3.modest](../model/GomX-3.modest).

The arrays have the following layout with every value in minutes starting from March 20, 2016, 05:00 UTC:

```transient int(0 .. 4320)[] profile = [start,end,start,end,...]```