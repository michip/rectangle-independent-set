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

Here are two examples on how to run the solver. The first one uses the recommended solver `cp-sat` while the second one uses `Gurobi`.

```bash
foo@bar:~$ rectis -s cp-sat -t 900 --out output.json instances/medium.csv 
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 496/496 [00:00<00:00, 243746.31it/s]


Starting CP-SAT solver v9.9.3963
Starting CP-SAT solver v9.9.3963
Parameters: max_time_in_seconds: 900 log_search_progress: true
Parameters: max_time_in_seconds: 900 log_search_progress: true
Setting number of workers to 10
Setting number of workers to 10


Initial optimization model '': (model_fingerprint: 0x6e7413c9eeb0ff31)
#Variables: 248 (#bools: 248 in objective)
  - 248 Booleans in [0,1]
#kBoolOr: 320 (#literals: 640)
Initial optimization model '': (model_fingerprint: 0x6e7413c9eeb0ff31)
#Variables: 248 (#bools: 248 in objective)
  - 248 Booleans in [0,1]
#kBoolOr: 320 (#literals: 640)


Starting presolve at 0.00s
Starting presolve at 0.00s
  8.50e-05s  0.00e+00d  [DetectDominanceRelations] 
  8.50e-05s  0.00e+00d  [DetectDominanceRelations] 
  3.18e-04s  0.00e+00d  [PresolveToFixPoint] #num_loops=6 #num_dual_strengthening=3 
  3.18e-04s  0.00e+00d  [PresolveToFixPoint] #num_loops=6 #num_dual_strengthening=3 
  2.00e-06s  0.00e+00d  [ExtractEncodingFromLinear] 
  2.00e-06s  0.00e+00d  [ExtractEncodingFromLinear] 
[Symmetry] Graph for symmetry has 680 nodes and 992 arcs.
[Symmetry] Graph for symmetry has 680 nodes and 992 arcs.
[Symmetry] Symmetry computation done. time: 0.000348 dtime: 0.00062559
[Symmetry] Symmetry computation done. time: 0.000348 dtime: 0.00062559
[Symmetry] #generators: 16, average support size: 26.25
[Symmetry] #generators: 16, average support size: 26.25
[Symmetry] 13 orbits with sizes: 32,16,16,16,16,16,16,16,16,16,...
[Symmetry] 13 orbits with sizes: 32,16,16,16,16,16,16,16,16,16,...
[Symmetry] Num fixable by binary propagation in orbit: 1 / 32
[Symmetry] Num fixable by binary propagation in orbit: 1 / 32
[Symmetry] Found orbitope of size 27 x 2
[Symmetry] Found orbitope of size 27 x 2
[SAT presolve] num removable Booleans: 0 / 216
[SAT presolve] num removable Booleans: 0 / 216
[SAT presolve] num trivial clauses: 0
[SAT presolve] num trivial clauses: 0
[SAT presolve] [0s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
[SAT presolve] [0s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
[SAT presolve] [1.7e-05s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
[SAT presolve] [1.7e-05s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
[SAT presolve] [2.8e-05s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
[SAT presolve] [2.8e-05s] clauses:280 literals:560 vars:216 one_side_vars:216 simple_definition:0 singleton_clauses:0
  2.66e-04s  9.52e-05d  [Probe] #probed=464 
  2.66e-04s  9.52e-05d  [Probe] #probed=464 
  1.03e-04s  0.00e+00d  [MaxClique] Merged 280(560 literals) into 136(344 literals) at_most_ones. 
  1.03e-04s  0.00e+00d  [MaxClique] Merged 280(560 literals) into 136(344 literals) at_most_ones. 
  1.50e-05s  0.00e+00d  [DetectDominanceRelations] 
  1.50e-05s  0.00e+00d  [DetectDominanceRelations] 
  1.15e-04s  0.00e+00d  [PresolveToFixPoint] #num_loops=9 #num_dual_strengthening=1 
  1.15e-04s  0.00e+00d  [PresolveToFixPoint] #num_loops=9 #num_dual_strengthening=1 
  1.00e-06s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.00e-06s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  5.00e-06s  0.00e+00d  [DetectDuplicateConstraints] 
  5.00e-06s  0.00e+00d  [DetectDuplicateConstraints] 
  1.00e-06s  0.00e+00d  [DetectDominatedLinearConstraints] 
  1.00e-06s  0.00e+00d  [DetectDominatedLinearConstraints] 
  1.00e-06s  0.00e+00d  [DetectDifferentVariables] 
  1.00e-06s  0.00e+00d  [DetectDifferentVariables] 
  2.00e-06s  0.00e+00d  [ProcessSetPPC] 
  2.00e-06s  0.00e+00d  [ProcessSetPPC] 
  2.00e-06s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  2.00e-06s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  5.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  5.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigVerticalLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigVerticalLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  1.00e-06s  0.00e+00d  [MergeClauses] 
  1.00e-06s  0.00e+00d  [MergeClauses] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
[Symmetry] Graph for symmetry has 248 nodes and 0 arcs.
[Symmetry] Graph for symmetry has 248 nodes and 0 arcs.
[Symmetry] Symmetry computation done. time: 6e-06 dtime: 1.488e-05
[Symmetry] Symmetry computation done. time: 6e-06 dtime: 1.488e-05
  8.00e-05s  2.69e-05d  [Probe] #probed=176 
  8.00e-05s  2.69e-05d  [Probe] #probed=176 
  2.00e-06s  0.00e+00d  [MaxClique] 
  2.00e-06s  0.00e+00d  [MaxClique] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.00e-06s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  1.00e-06s  0.00e+00d  [ProcessAtMostOneAndLinear] 
  3.00e-06s  0.00e+00d  [DetectDuplicateConstraints] 
  3.00e-06s  0.00e+00d  [DetectDuplicateConstraints] 
  0.00e+00s  0.00e+00d  [DetectDominatedLinearConstraints] 
  0.00e+00s  0.00e+00d  [DetectDominatedLinearConstraints] 
  0.00e+00s  0.00e+00d  [DetectDifferentVariables] 
  0.00e+00s  0.00e+00d  [DetectDifferentVariables] 
  1.00e-06s  0.00e+00d  [ProcessSetPPC] 
  1.00e-06s  0.00e+00d  [ProcessSetPPC] 
  1.00e-06s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  1.00e-06s  0.00e+00d  [FindAlmostIdenticalLinearConstraints] 
  5.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  5.00e-06s  0.00e+00d  [FindBigAtMostOneAndLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigVerticalLinearOverlap] 
  1.00e-06s  0.00e+00d  [FindBigVerticalLinearOverlap] 
  4.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  4.00e-06s  0.00e+00d  [FindBigHorizontalLinearOverlap] 
  1.00e-06s  0.00e+00d  [MergeClauses] 
  1.00e-06s  0.00e+00d  [MergeClauses] 
  4.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  4.00e-06s  0.00e+00d  [PresolveToFixPoint] 
  1.20e-05s  0.00e+00d  [ExpandObjective] 
  1.20e-05s  0.00e+00d  [ExpandObjective] 


Presolve summary:
Presolve summary:
  - 16 affine relations were detected.
  - 16 affine relations were detected.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 680 times.
  - rule 'TODO dual: only one unspecified blocking constraint?' was applied 680 times.
  - rule 'TODO symmetry: add symmetry breaking inequalities?' was applied 1 time.
  - rule 'TODO symmetry: add symmetry breaking inequalities?' was applied 1 time.
  - rule 'affine: new relation' was applied 16 times.
  - rule 'affine: new relation' was applied 16 times.
  - rule 'at_most_one: dominated singleton' was applied 24 times.
  - rule 'at_most_one: dominated singleton' was applied 24 times.
  - rule 'at_most_one: empty or all false' was applied 8 times.
  - rule 'at_most_one: empty or all false' was applied 8 times.
  - rule 'at_most_one: removed literals' was applied 192 times.
  - rule 'at_most_one: removed literals' was applied 192 times.
  - rule 'at_most_one: singleton' was applied 120 times.
  - rule 'at_most_one: singleton' was applied 120 times.
  - rule 'at_most_one: size one' was applied 128 times.
  - rule 'at_most_one: size one' was applied 128 times.
  - rule 'at_most_one: transformed into max clique.' was applied 1 time.
  - rule 'at_most_one: transformed into max clique.' was applied 1 time.
  - rule 'bool_and: dual equality.' was applied 8 times.
  - rule 'bool_and: dual equality.' was applied 8 times.
  - rule 'bool_and: x => x' was applied 16 times.
  - rule 'bool_and: x => x' was applied 16 times.
  - rule 'bool_or: implications' was applied 320 times.
  - rule 'bool_or: implications' was applied 320 times.
  - rule 'dual: enforced equivalence' was applied 8 times.
  - rule 'dual: enforced equivalence' was applied 8 times.
  - rule 'dual: fix variable' was applied 8 times.
  - rule 'dual: fix variable' was applied 8 times.
  - rule 'enforcement: literal not used' was applied 8 times.
  - rule 'enforcement: literal not used' was applied 8 times.
  - rule 'exactly_one: singleton' was applied 72 times.
  - rule 'exactly_one: singleton' was applied 72 times.
  - rule 'presolve: 160 unused variables removed.' was applied 1 time.
  - rule 'presolve: 160 unused variables removed.' was applied 1 time.
  - rule 'presolve: iteration' was applied 2 times.
  - rule 'presolve: iteration' was applied 2 times.


Presolved optimization model '': (model_fingerprint: 0xd34aa9d5618c87d8)
#Variables: 0 ( in objective)

Presolved optimization model '': (model_fingerprint: 0xd34aa9d5618c87d8)
#Variables: 0 ( in objective)



Preloading model.
Preloading model.
#Bound   0.00s best:-inf  next:[88,88]    initial_domain
#Bound   0.00s best:-inf  next:[88,88]    initial_domain
[Symmetry] Graph for symmetry has 0 nodes and 0 arcs.
[Symmetry] Graph for symmetry has 0 nodes and 0 arcs.
#Model   0.00s var:0/0 constraints:0/0
#Model   0.00s var:0/0 constraints:0/0


Starting search at 0.00s with 10 workers.
Starting search at 0.00s with 10 workers.
5 full problem subsolvers: [default_lp, max_lp, no_lp, quick_restart, quick_restart_no_lp]
5 full problem subsolvers: [default_lp, max_lp, no_lp, quick_restart, quick_restart_no_lp]
4 first solution subsolvers: [fj_long_default, fj_short_default, fs_random, fs_random_quick_restart]
4 first solution subsolvers: [fj_long_default, fj_short_default, fs_random, fs_random_quick_restart]
3 incomplete subsolvers: [feasibility_pump, rins/rens, violation_ls]
3 incomplete subsolvers: [feasibility_pump, rins/rens, violation_ls]
2 helper subsolvers: [neighborhood_helper, synchronization_agent]
2 helper subsolvers: [neighborhood_helper, synchronization_agent]
#1       0.00s best:88    next:[]         no_lp (fixed_bools=0/0)
#1       0.00s best:88    next:[]         no_lp (fixed_bools=0/0)
#Done    0.00s no_lp
#Done    0.00s no_lp
#Done    0.00s max_lp
#Done    0.00s max_lp
#Done    0.00s quick_restart
#Done    0.00s quick_restart


Task timing                          n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
               'default_lp':         1 [135.00us, 135.00us] 135.00us   0.00ns 135.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
         'feasibility_pump':         1 [  7.00us,   7.00us]   7.00us   0.00ns   7.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
          'fj_long_default':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
         'fj_short_default':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                'fs_random':         1 [ 89.00us,  89.00us]  89.00us   0.00ns  89.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
  'fs_random_quick_restart':         1 [ 31.00us,  31.00us]  31.00us   0.00ns  31.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                   'max_lp':         1 [148.00us, 148.00us] 148.00us   0.00ns 148.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                    'no_lp':         1 [134.00us, 134.00us] 134.00us   0.00ns 134.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
            'quick_restart':         1 [179.00us, 179.00us] 179.00us   0.00ns 179.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
      'quick_restart_no_lp':         1 [ 55.00us,  55.00us]  55.00us   0.00ns  55.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                'rins/rens':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
             'violation_ls':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns

Task timing                          n [     min,      max]      avg      dev     time         n [     min,      max]      avg      dev    dtime
               'default_lp':         1 [135.00us, 135.00us] 135.00us   0.00ns 135.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
         'feasibility_pump':         1 [  7.00us,   7.00us]   7.00us   0.00ns   7.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
          'fj_long_default':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
         'fj_short_default':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                'fs_random':         1 [ 89.00us,  89.00us]  89.00us   0.00ns  89.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
  'fs_random_quick_restart':         1 [ 31.00us,  31.00us]  31.00us   0.00ns  31.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                   'max_lp':         1 [148.00us, 148.00us] 148.00us   0.00ns 148.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                    'no_lp':         1 [134.00us, 134.00us] 134.00us   0.00ns 134.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
            'quick_restart':         1 [179.00us, 179.00us] 179.00us   0.00ns 179.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
      'quick_restart_no_lp':         1 [ 55.00us,  55.00us]  55.00us   0.00ns  55.00us         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
                'rins/rens':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns
             'violation_ls':         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns         0 [  0.00ns,   0.00ns]   0.00ns   0.00ns   0.00ns

Search stats                  Bools  Conflicts  Branches  Restarts  BoolPropag  IntegerPropag
               'default_lp':      0          0         0         0           0              0
                'fs_random':      0          0         0         0           0              0
  'fs_random_quick_restart':      0          0         0         0           0              0
                   'max_lp':      0          0         0         0           0              1
                    'no_lp':      0          0         0         0           0              1
            'quick_restart':      0          0         0         0           0              1
      'quick_restart_no_lp':      0          0         0         0           0              0

Search stats                  Bools  Conflicts  Branches  Restarts  BoolPropag  IntegerPropag
               'default_lp':      0          0         0         0           0              0
                'fs_random':      0          0         0         0           0              0
  'fs_random_quick_restart':      0          0         0         0           0              0
                   'max_lp':      0          0         0         0           0              1
                    'no_lp':      0          0         0         0           0              1
            'quick_restart':      0          0         0         0           0              1
      'quick_restart_no_lp':      0          0         0         0           0              0

SAT stats                     ClassicMinim  LitRemoved  LitLearned  LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
               'default_lp':             0           0           0             0         0         0           0         0          0            0        0
                'fs_random':             0           0           0             0         0         0           0         0          0            0        0
  'fs_random_quick_restart':             0           0           0             0         0         0           0         0          0            0        0
                   'max_lp':             0           0           0             0         0         0           0         0          0            0        0
                    'no_lp':             0           0           0             0         0         0           0         0          0            0        0
            'quick_restart':             0           0           0             0         0         0           0         0          0            0        0
      'quick_restart_no_lp':             0           0           0             0         0         0           0         0          0            0        0

SAT stats                     ClassicMinim  LitRemoved  LitLearned  LitForgotten  Subsumed  MClauses  MDecisions  MLitTrue  MSubsumed  MLitRemoved  MReused
               'default_lp':             0           0           0             0         0         0           0         0          0            0        0
                'fs_random':             0           0           0             0         0         0           0         0          0            0        0
  'fs_random_quick_restart':             0           0           0             0         0         0           0         0          0            0        0
                   'max_lp':             0           0           0             0         0         0           0         0          0            0        0
                    'no_lp':             0           0           0             0         0         0           0         0          0            0        0
            'quick_restart':             0           0           0             0         0         0           0         0          0            0        0
      'quick_restart_no_lp':             0           0           0             0         0         0           0         0          0            0        0

LNS stats       Improv/Calls  Closed  Difficulty  TimeLimit
  'rins/rens':           0/0      0%        0.50       0.10

LNS stats       Improv/Calls  Closed  Difficulty  TimeLimit
  'rins/rens':           0/0      0%        0.50       0.10

LS stats               Batches  Restarts  LinMoves  GenMoves  CompoundMoves  WeightUpdates
   'fj_long_default':        0         0         0         0              0              0
  'fj_short_default':        0         0         0         0              0              0
      'violation_ls':        0         0         0         0              0              0

LS stats               Batches  Restarts  LinMoves  GenMoves  CompoundMoves  WeightUpdates
   'fj_long_default':        0         0         0         0              0              0
  'fj_short_default':        0         0         0         0              0              0
      'violation_ls':        0         0         0         0              0              0

Solutions (1)    Num   Rank
       'no_lp':    1  [1,1]

Solutions (1)    Num   Rank
       'no_lp':    1  [1,1]

Objective bounds     Num
  'initial_domain':    1

Objective bounds     Num
  'initial_domain':    1

Solution repositories    Added  Queried  Ignored  Synchro
  'feasible solutions':      0        0        0        0
        'lp solutions':      0        0        0        0
                'pump':      0        0

Solution repositories    Added  Queried  Ignored  Synchro
  'feasible solutions':      0        0        0        0
        'lp solutions':      0        0        0        0
                'pump':      0        0

CpSolverResponse summary:
status: OPTIMAL
objective: 88
best_bound: 88
integers: 1
booleans: 0
conflicts: 0
branches: 0
propagations: 0
integer_propagations: 0
restarts: 0
lp_iterations: 0
walltime: 0.006394
usertime: 0.006394
deterministic_time: 0.00012208
gap_integral: 0
solution_fingerprint: 0xbeacb9ca26f13811

CpSolverResponse summary:
status: OPTIMAL
objective: 88
best_bound: 88
integers: 1
booleans: 0
conflicts: 0
branches: 0
propagations: 0
integer_propagations: 0
restarts: 0
lp_iterations: 0
walltime: 0.006394
usertime: 0.006394
deterministic_time: 0.00012208
gap_integral: 0
solution_fingerprint: 0xbeacb9ca26f13811

Found solution: 88.0
Best bound: 88.0
Optimal True
Writing solution to output.json
```

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