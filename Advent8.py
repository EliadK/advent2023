with open('input8.txt', 'r') as file:
    map=[[subsub.split(", ") for subsub in sub.split(" = (")][0][0] for sub in file.read().split("\n")[2:-1]]
with open('input8.txt', 'r') as file:
    instructions = file.read().split("\n")[:1][0]
with open('input8.txt', 'r') as file:
    L=[[subsub.split(", ") for subsub in sub.split(" = (")][1][0] for sub in file.read().split("\n")[2:-1]]
with open('input8.txt', 'r') as file:
    R = [[[subsubsub.split(")")[0] for subsubsub in subsub.split(", ")] for subsub in sub.split(" = (")][1][1] for sub in file.read().split("\n")[2:-1]]

n=0
ii=0
i=map.index("AAA")
while map[i] != "ZZZ":
    n += 1
    print (f"we're at {map[i]}")
    print(f"takeing a {instructions[ii]}")
    if instructions[ii]=="L":
        print(f"going to {L[i]}")
        i = map.index(L[i])
    if instructions[ii]=="R":
        i = map.index(R[i])
        print(f"going to {R[i]}")
    if ii == len(instructions)-1: ii=0
    else: ii+=1
print(f"number of steps is {n}")