# QEES

This project consists of two parts:

* Part 1 - A model checker is programmed in Python for costoptimal reachability properties on timed automata specified in Modest;
* Part 2 - That model checker is used to compute battery-aware experiment schedules for the GomX-3 nanosatellite;

## Part 1

During the first phase of the project a model checker has been created for unbounded and cost-optimal reachability properties for Modest models in Python.

### Prerequisites

The model checker is designed to run on Python 3.7 or newer.
The following package is required:

``` console
pip3 install plotly.express
```

### Execution

In order to run the model checker in Python, run [checker.py](checker.py) with a model.

An example of the files which can be ran by the checker are all the files with the *.py* extension that can be found in the folder [Part_1/modest_models](Part_1/modest_models).

An example execution of one of the files in [Part_1/modest_models](Part_1/modest_models) can be seen below:

```console
python3 checker.py /Part_1/modest_models/test1.py 
```

The following (optional) arguments are supported by the checker:

``` console
optional arguments:
  -h, --help  show this help message and exit
  --d         d(ebug): Enter runtime debug mode
  --t         t(race): Print the property trace
  --s         s(chedule): Create human-readable CSV schedules and KiBam baseload CSV
  --bfs       bfs: Use the Breadth First Search algorithm for the exist properties, default is DFS
  --dijkstra  dijkstra: Use Dijkstra algorithm for the Xmin properties, default is Best First Search
```

The model checker outputs:

* For every property of the form E<> *target* specified in the model, where *target* is a Boolean expression that does not contain further property operators, whether the model satisfies the property or not.
If requested by --t, the trace is also printed.
* For every property of the form Xmin(*cost-spec*, *target*) specified in the model, where *cost-spec* is of the form T(*rate-exp*) or S(*jump-exp*) with *rate-exp* and *jump-exp* numeric expressions not containing further property operators and *target* a Boolean expression not containing further property operators, whether a state satisfying *target* is reachable from the initial state, and if yes, the minimum cost of reaching it.
If requested by --t, the trace is also printed.

## Part 2

During the second phase of the project a Modest model was implemented to generate a safe, good, and non-trivial job schedule for the GomX-3 satellite for a nontrivial period of time between March 20, 2016, 05:00 UTC, and March 22, 2016, 22:00 UTC.

The final model [GomX-3.modest](Part_2/model/GomX-3.modest) is located in [Part_2/model](Part_2/model). In order to use the nanosattelite data in the *.csv* files in [Part_2/data](Part_2/data), a Python script was developed. This Python script converts the CSV data to transient arrays that can be used in the GomX-3 Modest model. Check the [README.md](Part_2/data/README.md) in the folder [Part_2/data](Part_2/data) for more information.

Refer to [schedule-instructions.txt](schedule-instructions.txt) to generate the final schedule. 

Refer to [report.txt](report.txt) to learn more about the Modest model [GomX-3.modest](Part_2/model/GomX-3.modest)

## Authors

* s2396335 - **Edian Annink** - *e.b.annink@student.utwente.nl*
* s2204320 - **Glen te Hofsté** - *g.tehofste@student.utwente.nl*
* s2613352 - **Kilian van Berlo** - *k.vanberlo@student.utwente.nl*
