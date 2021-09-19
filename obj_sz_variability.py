import sys
import matplotlib.pyplot as plt
import numpy as np
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
          'legend.fontsize': 32,
          'legend.handlelength': 2}
plt.rcParams.update(params)


def plot_dict(x, ohp, label, marker, every):

    keys = list(x.keys())
    keys.sort()

    vals = []
    for k in keys:
        vals.append(x[k])
    vals = np.cumsum(vals)

    plt.plot(keys, vals, label=label, marker=marker, markevery=every)


markers = ["o", "v", "s", "^", "<", ">", "p", "P", "1", "2", "3", "4", "+", "x", "X", "d", "D", ]    
for i in range(4):
    sz_dst = defaultdict(float)
    f = open("data/tc/each_class/iat_sz_" + str(i) + ".txt", "r")

    for l in f:
        l = l.strip().split(" ")
        if len(l) > 1:
            sz = int(float(l[0]))
            pr = float(l[1])
            sz_dst[sz] += pr

    if i == 0:
        label = "Download"
    elif i == 1:
        label = "Image"
    elif i == 2:
        label = "Media"
    elif i == 3:
        label = "Web"
    plot_dict(sz_dst, 0,label, markers[i], 1000)

plt.xlabel("Object size (Bytes)")
plt.ylabel("CDF")
plt.ylim([0, 1])
plt.gcf().subplots_adjust(left=0.15, bottom=0.15)
plt.legend()
plt.grid()
plt.xscale("log")
plt.savefig("obj_sz_variability.pdf")



            
