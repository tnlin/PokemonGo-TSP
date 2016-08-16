#coding:utf-8
import numpy as np
import json
from util import *
from export import *

def main():
    filename = "data/nctu.csv"
    #filename = "data/nthu.csv"
    #filename = "data/thu.csv"
    coordinates = np.loadtxt(filename, delimiter=',')

    # Params Initial
    num_location = coordinates.shape[0]
    markov_step = 10 * num_location
    T, T_MIN, T_ALPHA  = 100, 1, 0.99

    # Build distance matrix to accelerate cost computing
    distmat = get_distmat(coordinates)

    # States: New, Current and Best
    sol_new, sol_current, sol_best = (np.arange(num_location), ) * 3
    cost_new, cost_current, cost_best = (float('inf'), ) * 3

    # Record costs during the process
    costs = []

    # Simulated Annealing
    while T > T_MIN:
        for i in np.arange(markov_step):
            # Use three different methods to generate new solution
            # Swap, Reverse, and Transpose
            choice = np.random.randint(3)
            if choice == 0:
                sol_new = swap(sol_new)
            elif choice ==1:
                sol_new = reverse(sol_new)
            else:
                sol_new = transpose(sol_new)

            # Get the total distance of new route
            cost_new = sum_distmat(sol_new, distmat)

            if accept(cost_new, cost_current, T):
                # Update sol_current
                sol_current = sol_new.copy()
                cost_current = cost_new

                if cost_new < cost_best:
                    sol_best = sol_new.copy()
                    cost_best = cost_new
            else:
                sol_new = sol_current.copy()

        # Lower the temperature
        T *= T_ALPHA
        costs.append(cost_best)
        # Monitor the temperature & cost
        print("Temperature:", "%.2f°C" % round(T, 2), " Distance:", "%.2fm" % round(cost_best, 2))

    # Show final cost & route
    print("Final Distance:", round(costs[-1], 2))
    print("Best Route", sol_best)

    route = json.dumps(sol_best.tolist())
    payloads = [ costs[-1], route, markov_step ]

    # Save the result to sqlite
    save_sqlite(payloads)
    # Plot cost function and TSP-route
    plot(sol_best.tolist(), coordinates, costs)

    #export to path.json for google map
    export2json(filename)

if __name__ == "__main__":
    main()
