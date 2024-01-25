import re

with open("input14.txt", "r") as file:
    rock_map=file.read()

import time
t=time.process_time()

rock_map = rock_map.split("\n")
c = re.compile("O")
s = re.compile("#")
n=1
cache={}
for cycle in range(1000000000):
    key=tuple(rock_map)
    if key in cache:
        rock_map=list(cache[key])
        n+=1
        continue
    blockage=list([0]*len(rock_map[0]))
    line_number=0
    for line in rock_map:
        for match in s.finditer(line):
            blockage[match.start()]=line_number+1
        for match in c.finditer(line):
            m=match.start()
            rock_map[line_number]=rock_map[line_number][:m]+"."+rock_map[line_number][m+1:]
            rock_map[blockage[m]]=rock_map[blockage[m]][:m]+"O"+rock_map[blockage[m]][m+1:]
            blockage[m]+=1
        line_number += 1

    line_number=0
    for line in rock_map:
        line_blockage=list([0]*len(rock_map[0]))
        matches=list(c.finditer(line))
        block_index=0
        for match in s.finditer(line):
            line_blockage[match.start()] = "#"
        for match in matches:
            m=match.start()
            block_range=list(reversed(line_blockage))
            if "#" in block_range[len(line_blockage)-m:]:
                block_index=m-1-block_range[len(line_blockage)-m:].index("#")
                rock_map[line_number]=rock_map[line_number][:m]+"."+rock_map[line_number][m+1:]
                rock_map[line_number]=rock_map[line_number][:block_index+1]+"O"+rock_map[line_number][block_index+2:]
                line_blockage[block_index]=0
                line_blockage[block_index+1]="#"
            else:
                rock_map[line_number] = rock_map[line_number][:m] + "." + rock_map[line_number][m + 1:]
                rock_map[line_number] = "O" +rock_map[line_number][1:]
                line_blockage[0]="#"
        line_number += 1

    line_number=len(rock_map)-1
    blockage=list([len(rock_map)-1]*len(rock_map[0]))
    for line in reversed(rock_map):
        for match in s.finditer(line):
            blockage[match.start()]=line_number-1
        for match in c.finditer(line):
            m=match.start()
            rock_map[line_number]=rock_map[line_number][:m]+"."+rock_map[line_number][m+1:]
            rock_map[blockage[m]]=rock_map[blockage[m]][:m]+"O"+rock_map[blockage[m]][m+1:]
            blockage[m]-=1
        line_number -= 1

    line_number=0
    for line in rock_map:
        line_blockage=list([0]*len(rock_map[0]))
        matches=list(c.finditer(line))
        for match in s.finditer(line):
            line_blockage[match.start()] = "#"
        for match in reversed(matches):
            m=match.start()
            if "#" in line_blockage[m+1:]:
                block_index=m+1+line_blockage[m+1:].index("#")
                rock_map[line_number]=rock_map[line_number][:m]+"."+rock_map[line_number][m+1:]
                rock_map[line_number]=rock_map[line_number][:block_index-1]+"O"+rock_map[line_number][block_index:]
                line_blockage[block_index]=0
                line_blockage[block_index-1]="#"
            else:
                rock_map[line_number] = rock_map[line_number][:m] + "." + rock_map[line_number][m + 1:]
                rock_map[line_number] = rock_map[line_number][:-1] + "O"
                line_blockage[-1]="#"
        line_number += 1
    n+=1
    cache[key]=tuple(rock_map)

sum=0
line_number=len(rock_map)
for line in rock_map:
    for match in c.finditer(line):
        sum+=line_number
    line_number -= 1
print(sum)
print(time.process_time()-t)
print(len(cache))