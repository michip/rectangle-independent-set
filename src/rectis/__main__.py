import json

from rectis.solvers import run_solver, IndependentSetSolution
from rectis.utils.parser import read_instance


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Rectangle Independent Set Solver')
    parser.add_argument('-p', '--plot',
                        action="store_true", help='If set, plot the given file instead of running the solver')

    parser.add_argument('-s', '--solver',
                        type=str, default='cp-sat',
                        choices=['cp-sat', 'ip'], help='Solver to use for the optimization')
    parser.add_argument('-t', '--timeout',
                        type=int, default=900, help='Timeout in seconds')
    parser.add_argument('-o', '--out', type=str, help='Output file')
    parser.add_argument('input',
                        type=str, help='Input file')

    args = parser.parse_args()

    if args.plot:
        import matplotlib.pyplot as plt
        print("Plotting", args.input)
        with open(args.input, 'r') as f:
            data = json.load(f)

        solution = IndependentSetSolution.from_dict(data)

        fig, ax = plt.subplots()
        solution.plot(ax)
        #ax.set_aspect('equal')
        plt.show()
    else:
        rectangles = read_instance(args.input)

        solution = run_solver(args.solver, rectangles, args.timeout)

        print("Found solution:", solution.objective_value)
        print("Best bound:", solution.best_bound)
        print("Optimal", solution.optimal)

        if args.out:
            print("Writing solution to", args.out)
            with open(args.out, 'w') as f:
                json.dump(solution.to_dict(), f)


if __name__ == '__main__':
    main()
