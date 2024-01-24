import re

with open("input14.txt", "r") as file:
    rock_map=file.read()

import time
t=time.process_time()

rock_map=rock_map.split("\n")
blockage=list([len(rock_map)]*len(rock_map[0]))
c=re.compile("O")
s=re.compile("#")
sum=0
line_number=len(rock_map)
for line in rock_map:
    for match in s.finditer(line):
        blockage[match.start()]=line_number-1
    for match in c.finditer(line):
        blockage[match.start()]-=1
        sum+=blockage[match.start()]+1
    line_number -= 1
print(sum)
print(time.process_time()-t)