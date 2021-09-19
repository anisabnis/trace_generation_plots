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

#c_size = int(sys.argv[1]) * GB
c_sizes = [250*GB, 500*GB]
alg    = sys.argv[1]

if alg == "fifo":
    index = 2
elif alg == "lru":
    index = 4
elif alg == "random":
    index = 6
else:
    sys.exit()


generated_hr = defaultdict(list)
original_hr  = defaultdict(list)

traces = ["v", "w", "tc", "eu"]
## first populate generate
for c_size in c_sizes:
    for t in traces:
        
        f = open("./data/" + t + "/simulations/generated_stats_" + str(c_size) + "_all.txt", "r")
        for i in range(5):
            l = f.readline()

        req_objects = 0
        hit_objects = 0
    
        for l in f:
            l = l.strip().split()
            l = [int(x) for x in l]

            if len(l) > 0:
                req_objects += l[0]
                hit_objects += l[index]

        
        generated_hr[c_size].append(float(hit_objects)/req_objects)

for c_size in c_sizes:
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
                req_objects += l[0]
                hit_objects += l[index]

        original_hr[c_size].append(float(hit_objects)/req_objects)


original_hr[500*GB] = [original_hr[500*GB][i] - original_hr[250*GB][i] for i in range(len(original_hr[500*GB]))]
generated_hr[500*GB] = [generated_hr[500*GB][i] - generated_hr[250*GB][i] for i in range(len(generated_hr[500*GB]))]
barWidth = 0.20
#COLOR_FOUR = ["#eff3ff", "#bdd7e7", "#6baed6", "#2171b5", "#6baed6",  "#bdd7e7"]
COLOR_FOUR = ["darkgreen", "limegreen", "darkblue", "blue" ]
patterns = ["", "\\"]

x_pos = [x+1 for x in range(len(traces))]
fig, ax = plt.subplots()


bar1 = ax.bar([x-0.25 for x in x_pos], original_hr[250*GB], color=COLOR_FOUR[0], width=barWidth, hatch=patterns[0])
bar1above = ax.bar([x-0.25 for x in x_pos], original_hr[500*GB], color=COLOR_FOUR[1], bottom=original_hr[250*GB],width=barWidth, hatch=patterns[1])

bar2 = ax.bar([x+0.05 for x in x_pos], generated_hr[250*GB], color=COLOR_FOUR[2],width=barWidth, hatch=patterns[0])
bar2above = ax.bar([x+0.05 for x in x_pos], generated_hr[500*GB], color=COLOR_FOUR[3],width=barWidth, bottom=generated_hr[250*GB], hatch=patterns[1])

leg1 = ax.legend([bar1, bar2],['original','generated'], loc='upper right')
leg2 = ax.legend([bar1, bar1above],['250GB','500GB'], loc='upper left')
ax.add_artist(leg1)

plt.xticks(x_pos, traces)
plt.ylim([0, 1])
plt.ylabel("Request hitrate")
plt.grid()
plt.savefig("rhr_simulations_" + str(alg) + "_" + str(c_size/GB) + ".pdf")



    

    
        
