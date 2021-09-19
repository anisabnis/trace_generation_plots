import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

size=38
params = {'legend.fontsize': 'large',
          'figure.figsize': (12,8),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size-12,
          'ytick.labelsize': size,
          "lines.linewidth": 4, 
          'axes.titlepad': 30, 
          'lines.markersize': 12, 
          'legend.fontsize': 28,
          'legend.handlelength': 2}
plt.rcParams.update(params)

d = "data/"
TB = 1000000000

f = open(d + "/v/footprint_desc_all.txt", "r")
l = f.readline()
l = l.strip().split(" ")

byte = float(l[1])
time_diff = int(l[3]) - int(l[2])
byte_rate = float(byte)/time_diff

dst_generated = []
dst_original = []
for i in range(1,11):

    f = open(d + "v/age_dst/" + "age_distribution_generated_" + str(250*i) + ".txt", "r")
    l = f.readline()
    l = float(l.strip())
    dst = l/byte_rate 
    dst_generated.append(dst)
    f.close()

    f = open(d + "v/age_dst/" + "age_distribution_original_" + str(250*i) + ".txt", "r")
    l = f.readline()
    l = float(l.strip())
    dst = l/byte_rate 
    dst_original.append(dst)
    f.close()

plt.plot(dst_generated, marker="s", label="generated")
plt.plot(dst_original, marker="^", label="original")
plt.grid()
plt.ylabel("Eviction age (seconds)")
plt.xlabel("Cache size (TB)")
plt.xticks(range(10), [0.25*i for i in range(1,11)],rotation="vertical")
plt.gcf().subplots_adjust(left=0.2, bottom=0.2)
plt.legend()
plt.savefig("eviction_age.pdf")
