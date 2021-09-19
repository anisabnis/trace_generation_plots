import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

type = sys.argv[1]

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

## size distribution
traces = ["v", "w", "tc", "eu"]
i = 0
for t in traces:
    ## generated
    f = open("data/" + str(t) + "/generated/" + type + "_sz_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0])/10)*10] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-gen", marker=markers[i], markevery=1000)
    i += 1

    ## original
    f = open("data/" + t + "/sz_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0])/10)*10] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-orig", marker=markers[i], markevery=800)
    i += 1
plt.xscale("log")
plt.legend()
plt.grid()
plt.savefig("sz_dst.pdf")
plt.clf()


## popularity distribution
traces = ["v", "w", "tc", "eu"]
i = 0
for t in traces:
    ## generated
    f = open("data/" + str(t) + "/generated/" + type + "_pop_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0]))] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-gen", marker=markers[i], markevery=1000)
    i += 1

    ## original
    f = open("data/" + t + "/pop_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0]))] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-orig", marker=markers[i], markevery=800)
    i += 1
plt.xscale("log")
plt.legend()
plt.grid()
plt.savefig("pop_dst.pdf")
plt.clf()





## request sz distribution
traces = ["v", "w", "tc", "eu"]
i = 0
for t in traces:
    ## generated
    f = open("data/" + str(t) + "/generated/" + type + "_req_sz_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0])/10)*10] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-gen", marker=markers[i], markevery=1000)
    i += 1

    ## original
    f = open("data/" + t + "/req_sz_dst.txt", "r")
    sum_pr = 0
    sz_dst = defaultdict(int)
    for l in f:
        l = l.strip().split(" ")
        sz_dst[int(float(l[0])/10)*10] += int(l[1])
        pr = int(l[1])
        sum_pr += pr
    
    sz_keys = list(sz_dst.keys())
    sz_keys.sort()
    sz_dst1 = []
    for sz in sz_keys:
        pr = sz_dst[sz] 
        sz_dst1.append(float(pr)/sum_pr)
        
    sz_dst = np.cumsum(sz_dst1)
    plt.plot(sz_keys, sz_dst, label=t+"-orig", marker=markers[i], markevery=800)
    i += 1
plt.xscale("log")
plt.legend()
plt.grid()
plt.savefig("req_sz_dst.pdf")

    

