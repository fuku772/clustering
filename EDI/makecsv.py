import pandas as pd
import os
import glob

#os.chdir('/Users/username/downloads/dirname')

df = pd.DataFrame(columns = [])

for i in glob.glob("*.csv*"):
    tmp = pd.read_csv(i)
    df = pd.concat([df, tmp])

print(df)