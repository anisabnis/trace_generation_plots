import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

size=38
params = {'legend.fontsize': 'large',
          'figure.figsize': (12,8),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size,
          'ytick.labelsize': size,
          "lines.linewidth": 4, 
          'axes.titlepad': 30, 
          'lines.markersize': 15, 
          'legend.fontsize': 36,
          'legend.handlelength': 2}
plt.rcParams.update(params)

d = "data/"
GB = 1000000


c_size = int(sys.argv[1]) * GB
alg    = sys.argv[2]

if alg == "fifo":
    index = 2
elif alg == "lru":
    index = 4
elif alg == "random":
    index = 6
else:
    sys.exit()


markers = ["o", "v", "s", "^", "<", ">", "p", "P", "1", "2", "3", "4", "+", "x", "X", "d", "D", ]
i = 0
traces = ["v", "w", "tc", "eu"]
traces_all = ["Video", "Web", "TC", "EU"]
## first populate generate
for t in traces:
    f = open("./data/" + t + "/simulations/generated_stats_" + str(c_size) + "_all.txt", "r")
    for jj in range(5):
        l = f.readline()

    req_objects = 0
    hit_objects = 0

    hitrate = []
    
    for l in f:
        l = l.strip().split()
        l = [int(x) for x in l]

        if len(l) > 0:
            req_objects += l[0]
            hit_objects += l[index]        
            hitrate.append(float(hit_objects)/req_objects)


    hitrate = hitrate[:5000]
    plt.plot(hitrate, label=str(traces_all[i]), marker=markers[i],markevery=500)
    i += 1

plt.grid()
plt.ylim([0,1])
plt.ylabel("Request hitrate")
plt.xlabel("Number requests (x 10^5)")
plt.legend(loc=4)
plt.gcf().subplots_adjust( bottom=0.15)
plt.savefig("convergence_rhr.pdf")
