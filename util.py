import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
def plot(path, points, costs):
    '''
    path: List of the different orders in which the nodes are visited
    points: coordinates for the different nodes
    '''
    plt.figure(figsize=(15,6))

    plt.subplot(121)
    curve, = plt.plot(np.array(costs), label='Distance(m)')
    plt.ylabel("Distance")
    plt.xlabel("Iteration")
    plt.grid(True)
    plt.legend()
    plt.title("Final Distance: " + str(costs[-1]))

    plt.subplot(122)
    # Transform back to longitude/latitude
    points = (points / 111000).tolist()

    # Unpack the primary path and transform it into a list of ordered coordinates
    x = []; y = []
    for i in path:
        x.append(points[i][1])
        y.append(points[i][0])
    x.append(points[path[0]][1])
    y.append(points[path[0]][0])

    # Plot line
    plt.plot(x, y, 'c-', label='Route')

    # Plot dot
    plt.plot(x, y, 'bo', label='Location')

    # Avoid scientific notation
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

    # Set axis too slitghtly larger than the set of x and y
    plt.xlim(min(x)*0.99999, max(x)*1.00001)
    plt.ylim(min(y)*0.99999, max(y)*1.00001)
    plt.xlabel("Longitude")
    plt.ylabel("Lantitude")
    plt.title("TSP Route Visualization")
    plt.grid(True)
    plt.legend()
    plt.show()


