from collections import defaultdict
import sys

d = "data"
tc = sys.argv[1]

TB = 1000000000
up_lim = 10*TB
if tc == "tc":
    up_lim = 1.5*TB
elif tc == "w":
    up_lim = 3*TB

orig_prs = defaultdict(lambda : 0)
f = open(d + "/" + tc + "/" + "byte_footprint_desc_" +str("all") + ".txt", "r")
l = f.readline()
for l in f:
    l = l.strip().split(" ")
    key = int(l[1])
    pr = float(l[2])
    if key < up_lim:
        orig_prs[key] += pr
f.close()


gen_prs = defaultdict(lambda : 0)
f = open(d + "/" + tc + "/generated/" + "byte_footprint_desc_" +str("all") + ".txt", "r")
l = f.readline()
for l in f:
    l = l.strip().split(" ")
    key = int(l[1])
    pr = float(l[2])
    if key < up_lim:
        gen_prs[key] += pr
f.close()

all_keys = list(orig_prs.keys())
all_keys_n = list(gen_prs.keys())
all_keys.extend(all_keys_n)
all_keys = list(set(all_keys))
diff = 0
for k in all_keys:
    diff += abs(orig_prs[k] - gen_prs[k])

print(diff)
