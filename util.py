from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def plot_dict(x, label="-"):
    keys = list(x.keys())
    keys.sort()

    vals = []
    for k in keys:
        vals.append(x[k])
    
    sum_vals = sum(vals)
    vals = [float(x)/sum_vals for x in vals]
    vals = np.cumsum(vals)

    return keys, vals
    #plt.plot(keys, vals, label=label)#, marker="^", markersize=3, markevery=500)


def plot_list(x, label="-", maxlim=100000000000):
    a = defaultdict(int)
    for v in x:
        if v < maxlim:
            a[v] += 1

    return plot_dict(a, label)
