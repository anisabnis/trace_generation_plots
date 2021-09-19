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
          'lines.markersize': 16, 
          'legend.fontsize': 28,
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

    #keys.append(keys[-1] + 200000)
    keys = [float(x)/TB for x in keys]
    #sum_vals = sum(vals)
    #vals = [float(y)/sum_vals for y in vals]
    #vals = [(1-ohp)*y for y in vals]
    #vals.append(ohp)
    vals = np.cumsum(vals)

    plt.plot(keys, vals, label=label, marker=marker, markevery=every)


def plot_list(x, ohp, label, marker, every, maxlim=100*TB):
    a = defaultdict(int)
    for v in x:
        if v < maxlim:
            a[v] += 1
    plot_dict(a, ohp, label, marker, every)


def plot_orig(arg, label, marker, every):
    f = open(d + "/eu/byte_footprint_desc_" +str(arg) + ".txt", "r")
    l = f.readline()
    l = l.strip().split(" ")
    one_hits_pr = float(l[-1])/float(l[1])
    prs = defaultdict(lambda : 0)
    total_pr = 0
    max_key = 0

    for l in f:
        l = l.strip().split(" ")
        key = int(l[1])
        pr = float(l[2])
        if key > 100*TB:
            one_hits_pr += pr
        else:
            prs[key] += pr
        total_pr += pr
        if key > max_key:
            max_key = key

    plot_dict(prs, one_hits_pr, label, marker, every)
    return one_hits_pr, max_key

def plot_calculus(arg, label, marker, every):
    f = open(d + "/eu/calculus_byte_footprint_desc_" + str(arg) + ".txt", "r")
    l = f.readline()
    l = l.strip().split(" ")

    one_hits_pr = float(l[-1])/float(l[1])
    prs = defaultdict(lambda : 0)

    total_pr = 0

    max_key = 0
    for l in f:
        l = l.strip().split(" ")
        key = int(l[1])
        pr = float(l[2])
        if key > 10*TB:
            one_hits_pr += pr
        else:
            prs[key] += pr
        total_pr += pr
        if key > max_key:
            max_key = key

    plot_dict(prs, one_hits_pr, label, marker, every)
    return one_hits_pr, max_key


markers = ["o", "v", "s", "^", "<", ">", "p", "P", "1", "2", "3", "4", "+", "x", "X", "d", "D", ]
i = 0
one_hit_pr, max_key = plot_orig("01", "Media0+Media1(trace)", markers[i],5000)
one_hit_pr, max_key = plot_calculus("01", "Media0+Media1(calculus)", markers[i+1],10000)
i+= 2

one_hit_pr, max_key = plot_orig("02", "Media0+Media2(trace)", markers[i], 5000)
one_hit_pr, max_key = plot_calculus("02", "Media0+Media2(calculus)", markers[i+1], 10000)
i += 2

# one_hit_pr, max_key = plot_orig("012", "eu0+eu1+eu2(trace)", markers[i], 3000)
# one_hit_pr, max_key = plot_calculus("012", "eu0+eu1+eu2(calculus)", markers[i+1], 4000)
# i += 2



plt.ylabel("Byte hitrate (bhr)")
plt.xlabel("Cache size (TB)")
plt.grid()
plt.legend()
plt.gcf().subplots_adjust(left=0.20, bottom=0.15)
plt.ylim([0.,1])
plt.savefig("bfd_calculus.pdf")
