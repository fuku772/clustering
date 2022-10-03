from dataclasses import replace
from turtle import Turtle
from distance_func import make_distance

csv1='ABW_0_0.csv'
csv2='ABW_2_0.csv'

val=make_distance(csv1,csv2,values=True)

print(val)

import re
alist=[]
for i in range(len(val)):
    a=re.sub(r"\D","",val[i][0][-2:])
    alist.append(int(a))
print(alist)