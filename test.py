import timeit
import polars as pl

startTime = timeit.default_timer()
df1 = pl.scan_csv("./transactions_data.csv", low_memory=True).collect()
df2 = pl.scan_csv("./cards_data.csv", low_memory=True).collect()
df3 = pl.scan_csv("./users_data.csv", low_memory=True).collect()
endTime = timeit.default_timer()

df = [df1, df2, df3]

# print(df1.describe())
# print(df1.null_count())

for i in df: print(len(i))
for i in df: print(i.sample(n = int((len(i) * 50) / 100)))

print(f"Time: {endTime - startTime}")
