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


traces = ["v", "w", "tc", "eu"]
trace = ["Video", "Web", "TC", "EU"]
i = 0
## first populate generate
for t in traces:
    f = open("./data/" + t + "/simulations/byte_generated_stats_" + str(c_size) + "_all.txt", "r")
    for jj in range(5):
        l = f.readline()

    req_objects = 0
    hit_objects = 0

    hitrate = []
    
    for l in f:
        l = l.strip().split()
        l = [int(x) for x in l]

        if len(l) > 0:
            req_objects += l[1]
            hit_objects += l[index+1]        
            hitrate.append(float(hit_objects)/req_objects)

    if t == "v":
        hr = hitrate[-1]
        hitrate.extend([hr] * (5000 - len(hitrate)))

    hitrate = hitrate[:4999]                       
    plt.plot(hitrate, label=str(trace[i]), marker=markers[i],markevery=500)
    i += 1

plt.grid()
plt.ylim([0,1])
plt.ylabel("Byte hitrate")
plt.xlabel("Number requests (x 10^5)")
plt.legend()
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig("convergence_bhr.pdf")
