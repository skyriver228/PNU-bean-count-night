import pandas as pd

res_count = pd.read_excel("./Open/Kong_Open_True.xlsx", skiprows=1)
count = list(res_count["amount"])
f = open("count.txt", 'w')
for i in range(len(count)):
    data = count[i]
    f.write(str(data)+" ")
f.close()