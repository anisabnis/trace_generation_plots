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
          'lines.markersize': 12, 
          'legend.fontsize': 28,
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


generated_hr = []
original_hr  = []

traces = ["v", "w", "tc", "eu"]
## first populate generate
for t in traces:
    f = open("./data/" + t + "/simulations/byte_generated_stats_" + str(c_size) + "_all.txt", "r")
    for i in range(5):
        l = f.readline()

    req_objects = 0
    hit_objects = 0
    
    for l in f:
        l = l.strip().split()
        l = [int(x) for x in l]

        if len(l) > 0:
            req_objects += l[1]
            hit_objects += l[index+1]

        
    generated_hr.append(float(hit_objects)/req_objects)

for t in traces:
    f = open("./data/" + t + "/simulations/original.stats_" + str(c_size) + ".txt", "r")
    for i in range(5):
        l = f.readline()

    req_objects = 0
    hit_objects = 0
    
    for l in f:
        l = l.strip().split()
        l = [int(x) for x in l]

        if len(l) > 0:
            req_objects += l[1]
            hit_objects += l[index+1]

    original_hr.append(float(hit_objects)/req_objects)


barWidth = 0.20
COLOR_FOUR = ["#eff3ff", "#bdd7e7", "#6baed6", "#2171b5"]

x_pos = [x+1 for x in range(len(traces))]
fig, ax = plt.subplots()

ax.bar([x-0.25 for x in x_pos], original_hr, color=COLOR_FOUR[2], label="original-trace",width=barWidth)
ax.bar([x+0.05 for x in x_pos], generated_hr, color=COLOR_FOUR[3], label="generated-trace",width=barWidth)

plt.legend()
plt.xticks(x_pos, traces)
plt.ylim([0, 1])
plt.ylabel("Byte hitrate")
plt.grid()
plt.savefig("bhr_simulations_" + str(alg) + "_" + str(c_size/GB) + ".pdf")



    

    
        
