#coding:utf-8
import numpy as np
import sqlite3
import json
from util import plot

def sum_distmat(p, distmat):
    dist = 0
    num = p.shape[0]
    for i in range(num-1):
        dist += distmat[p[i]][p[i+1]]
    dist += distmat[p[0]][p[num-1]]
    return dist

def get_distmat(p):
    num = p.shape[0]
    # 1 degree of lat/lon ~ 111km = 111000m in Taiwan
    p *= 111000
    distmat = np.zeros((num, num))
    for i in range(num):
        for j in range(i, num):
            distmat[i][j] = distmat[j][i] = np.linalg.norm(p[i] - p[j])
    return distmat

def swap(sol_new):
    while True:
        n1 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        n2 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        if n1 != n2:
            break
    sol_new[n1], sol_new[n2] = sol_new[n2], sol_new[n1]
    return sol_new

def reverse(sol_new):
    while True:
        n1 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        n2 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        if n1 != n2:
            break
    sol_new[n1:n2] = sol_new[n1:n2][::-1]

    return sol_new

def transpose(sol_new):
    while True:
        n1 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        n2 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        n3 = np.int(np.floor(np.random.uniform(0, sol_new.shape[0])))
        if n1 != n2 != n3 != n1:
            break
    #Let n1 < n2 < n3
    n1, n2, n3 = sorted([n1, n2, n3])

    #Insert data between [n1,n2) after n3
    tmplist = sol_new[n1:n2].copy()
    sol_new[n1 : n1+n3-n2+1] = sol_new[n2 : n3+1].copy()
    sol_new[n3-n2+1+n1 : n3+1] = tmplist.copy()
    return sol_new

def accept(cost_new, cost_current, T):
    # If new cost better than current, accept it
    # If new cost not better than current, accept it by probability P(dE)
    # P(dE) = exp(dE/(kT)), defined by thermodynamics
    return ( cost_new < cost_current or
             np.random.rand() < np.exp(-(cost_new - cost_current) / T) )

def save_sqlite(payloads):
    conn = sqlite3.connect('data/tsp.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS TSP (costs REAL, route TEXT, markov_step INTEGER) ")
    c.execute('INSERT INTO TSP VALUES (?,?,?)' , payloads)
    conn.commit()
    conn.close()


def main():
    filename = "data/pokestops.csv"
    coordinates = np.loadtxt(filename, delimiter=',')

    # Params Initial
    num = coordinates.shape[0]
    markov_step = 10 * num
    T, T_MIN, T_ALPHA  = 100, 1, 0.99

    # Build distance matrix to accelerate cost computing
    distmat = get_distmat(coordinates)

    # States: New, Current and Best
    sol_new, sol_current, sol_best = (np.arange(num), ) * 3
    cost_new, cost_current, cost_best = (np.max, ) * 3

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
        print(T, cost_best)

    # Show final cost & route
    print(costs[-1], sol_best)

    route = json.dumps(sol_best.tolist())
    payloads = [ costs[-1], route, markov_step ]

    # Save the result to sqlite
    save_sqlite(payloads)
    # Plot cost function and TSP-route
    plot(sol_best.tolist(), coordinates, costs)

if __name__ == "__main__":
    main()
