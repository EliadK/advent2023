import re

with open("input11.txt","r") as file:
    nightsky=[line for line in file.read().split("\n")]
galaxies=[[],[]]

# map out galaxies as coords [line,spot]
#decided to use regex in order to learn and practice regex


# Make galaxy map
galaxy = re.compile("#")

for index,line in enumerate(nightsky):
    n=galaxy.search(line)
    while n:
        galaxies[0].append(index)
        galaxies[1].append(n.span()[0])
        n=galaxy.search(line,n.span()[1])

# Expand the space
n=0
i=0
while n < len(nightsky[0]):
    if galaxies[1].count(i) == 0:
        print(f"no galaxy at row{i}")
        for index,line in enumerate(nightsky):
            nightsky[index]=line[:n] + 999999*"." + line[n:]
        n+=999999
    n+=1
    i+=1

spacewarp=[]
n=0
i=0
while n < len(nightsky):
    if galaxies[0].count(i) == 0:
        print(f"no galaxy at {i}")
        spacewarp.append(n)
        for item in range(1, 1000000):
            nightsky.insert(n,nightsky[n])
            n+=1
    n+=1
    i+=1

# Recalculate galaxies for distance

galaxies=[]
i=0
while i<len(nightsky):
    if i in spacewarp:
        print("skipping")
        i+=1000000
        continue
    print(i)
    n=galaxy.search(nightsky[i])
    while n:
        galaxies.append([i,n.span()[0]])
        n=galaxy.search(nightsky[i],n.span()[1])
    i+=1

print("distance")
n=0
distance=0
while n<len(galaxies):
    i=n+1
    while i<len(galaxies):
        distance+= abs(galaxies[n][1]-galaxies[i][1]) + abs(galaxies[n][0]-galaxies[i][0])
        i+=1
    n+=1
print(distance)