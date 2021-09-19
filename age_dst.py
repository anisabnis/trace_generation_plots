import sys
import matplotlib.pyplot as plt
import numpy as np
from util import *
from collections import defaultdict


markers = ["o", "v", "s", "^", "<", ">", "p", "P", "1", "2", "3", "4", "+", "x", "X", "d", "D", ]
size=38
params = {'legend.fontsize': 'large',
          'figure.figsize': (12,8),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size,
          'ytick.labelsize': size,
          "lines.linewidth": 2, 
          'axes.titlepad': 30, 
          'lines.markersize': 8, 
          'legend.fontsize': 28,
          'legend.handlelength': 2}
plt.rcParams.update(params)

i = 0
## size distribution
#traces = ["v", "w", "tc", "eu"]
traces = ["v"]
for t in traces:
    f = open("data/" + t + "/eviction_ages/age_distribution_original.txt", "r")
    l = f.readline()
    l = l.strip().split(",")
    l = l[:-1]
    l = [int(x) for x in l]
    l = l[:int(len(l)/2)]
    keys, vals = plot_list(l)
    print(len(keys), len(vals))
    plt.plot(keys, vals, label=t+"-orig", marker=markers[i], markevery=200)
    i += 1

    f = open("data/" + t + "/eviction_ages/age_distribution_generated.txt", "r")
    l = f.readline()
    l = l.strip().split(",")
    l = l[:-1]
    l = [int(x) for x in l]
    l = l[:int(len(l)/2)]
    keys, vals = plot_list(l)
    plt.plot(keys, vals, label=t+"-gen", marker=markers[i], markevery=200)
    i += 1

plt.xscale("log")
plt.xlabel("Eviction age")
plt.ylabel("cdf")
plt.grid()
plt.legend()
plt.savefig("eviction_age.pdf")


