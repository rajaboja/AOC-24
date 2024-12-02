import sys
import pandas as pd

fp = sys.argv[1]

df = pd.read_csv(fp, sep="\s+", header=None, dtype=int)

df[0] = df[0].sort_values().values
df[1] = df[1].sort_values().values

print((df[0] - df[1]).abs().sum()) #answer 1

counts = df[1].value_counts().to_dict()

print((df[0].map(counts).fillna(0) * df[0]).sum()) #answer 2
