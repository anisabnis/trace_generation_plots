import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

size=38
params = {'legend.fontsize': 'large',
          'figure.figsize': (12,8),
          'axes.labelsize': size + 6,
          'axes.titlesize': size,
          'xtick.labelsize': size,
          'ytick.labelsize': size,
          "lines.linewidth": 4, 
          'axes.titlepad': 30, 
          'lines.markersize': 12, 
          'legend.fontsize': 36,
          'legend.handlelength': 2}
plt.rcParams.update(params)

d = "data/"
TB = 1000000000

def plot_dict(x, ohp, label, marker, every):

    keys = list(x.keys())
    keys.sort()

    vals = []
    for k in keys:
        vals.append(x[k])

    keys = [float(x)/TB for x in keys]
    # keys.append(keys[-1] + 200000)

    # sum_vals = sum(vals)
    # vals = [float(y)/sum_vals for y in vals]
    # vals = [(1-ohp)*y for y in vals]
    # vals.append(ohp)
    vals = np.cumsum(vals)

    plt.plot(keys, vals, label=label, marker=marker, markevery=every)


def plot_list(x, ohp, label, marker, every, maxlim=100*TB):
    a = defaultdict(int)
    for v in x:
        if v < maxlim:
            a[v] += 1
    plot_dict(a, ohp, label, marker, every)


def plot_orig(arg1 ,arg2, label, marker, every):
    if label == "orig":
        if arg2 == "req":
            f = open(d + "/" + arg1 + "/" + "footprint_desc_" +str("all") + ".txt", "r")
        else:
            f = open(d + "/" + arg1 + "/" + "byte_footprint_desc_" +str("all") + ".txt", "r")
    elif label == "lrusm":
        if arg2 == "req":
            f = open(d + "/" + arg1 + "/generated/" + "footprint_desc_" +str("lrusm_unit") + ".txt", "r")
        else:
            f = open(d + "/" + arg1 + "/generated/" + "byte_footprint_desc_" +str("lrusm_unit") + ".txt", "r")

    l = f.readline()
    l = l.strip().split(" ")

    if arg2 == "req":
        one_hits_pr = float(l[-2])/float(l[0])
    else:
        one_hits_pr = float(l[-1])/float(l[1])
        
    prs = defaultdict(lambda : 0)
    total_pr = 0
    max_key = 0

    up_lim = 10*TB
    if arg1 == "tc":
        up_lim = 1.5*TB
    elif arg1 == "w":
        up_lim = 3*TB

    for l in f:
        l = l.strip().split(" ")
        key = int(l[1])
        pr = float(l[2])
        if key > up_lim:
            one_hits_pr += pr
        else:
            prs[key] += pr
        total_pr += pr
        if key > max_key:
            max_key = key

    if arg2 == "req":
        l1 = "RHR"            
    else:
        l1 = "BHR"

    if label == "lrusm":
        l2 = "Lrusm"
    else:
        l2 = "Orig"
            
    plot_dict(prs, one_hits_pr, l2+":"+l1, marker, every)
    return one_hits_pr, max_key

markers = ["o", "v", "s", "^", "<", ">", "p", "P", "1", "2", "3", "4", "+", "x", "X", "d", "D", ]
i = 0

plot_orig("v", "req", "lrusm", markers[i], 10000)
i+= 1
plot_orig("v", "byte", "lrusm", markers[i], 10000)
i+= 1
plot_orig("v", "req", "orig", markers[i], 10000)
i+= 1
plot_orig("v", "byte", "orig", markers[i], 10000)
i+= 1


plt.ylabel("Hitrate")
plt.xlabel("Cache size (TB)")
plt.grid()
plt.legend()
plt.gcf().subplots_adjust(left=0.15, bottom=0.15)
plt.ylim([0.,1])
plt.savefig("lrusm_unit.pdf")


