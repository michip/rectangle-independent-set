# Rectis

This repository contains the code for solving an independent set problem
for intersection graphs of intersecting rectangles.

## Installation

To install the package, run the following command:

```bash
pip install .
```

There are two solvers available: `cp-sat` and `ip`. The `cp-sat` solver uses the
[Google OR-Tools](https://developers.google.com/optimization) library, while the `ip` solver uses the
[Gurobi](https://www.gurobi.com/) software package.
To use Gurobi, you need to have valid license. There are academic licenses available for free.

## Tests

To run the tests, run the following command in the root directory of this project

```bash
pytest
```

## Usage

To use the package, run either one of the following commands: `rectis` or `python -m rectis`.

```bash
rectis --help
usage: rectis [-h] [-p] [-s {cp-sat,ip}] [-t TIMEOUT] [-o OUT] input

Rectangle Independent Set Solver

positional arguments:
  input                 Input file

optional arguments:
  -h, --help            show this help message and exit
  -p, --plot            If set, plot the given file instead of running the solver
  -s {cp-sat,ip}, --solver {cp-sat,ip}
                        Solver to use for the optimization
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds
  -o OUT, --out OUT     Output file
```

After the package is installed you can also call the solver from Python code:

```python
from rectis.utils.parser import read_instance
from rectis.solvers import run_solver

rectangles = read_instance("path/to/instance")
solution = run_solver(rectangles=rectangles,
                      solver="cp-sat", # or "ip"
                      timeout=60) # timeout in seconds
```

## Example

Here is an example of how to run the solver:

```bash
foo@bar:~$ rectis -s ip -t 900 --out output.json instances/medium.csv    
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 496/496 [00:00<00:00, 306523.47it/s]
Set parameter Username
Academic license - for non-commercial use only - expires 2025-02-19
Set parameter TimeLimit to value 900
Gurobi Optimizer version 11.0.1 build v11.0.1rc0 (mac64[arm] - Darwin 22.6.0 22G630)

CPU model: Apple M1 Pro
Thread count: 10 physical cores, 10 logical processors, using up to 10 threads

Optimize a model with 472 rows, 248 columns and 944 nonzeros
Model fingerprint: 0xbb39aa8f
Variable types: 0 continuous, 248 integer (248 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [1e+00, 1e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 1e+00]
Found heuristic solution: objective 88.0000000
Presolve removed 472 rows and 248 columns
Presolve time: 0.00s
Presolve: All rows and columns removed

Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 1 (of 10 available processors)

Solution count 1: 88 

Optimal solution found (tolerance 1.00e-04)
Best objective 8.800000000000e+01, best bound 8.800000000000e+01, gap 0.0000%
Found solution: 88.0
Best bound: 88.0
Optimal True
Writing solution to output.json
```

## Plotting a solution

If you want to plot a solution, you can use the following command:

```bash
foo@bar:~$ rectis --plot output.json
Plotting output.json
```