with open('input8.txt', 'r') as file:
    map=[[subsub.split(", ") for subsub in sub.split(" = (")][0][0] for sub in file.read().split("\n")[2:-1]]
with open('input8.txt', 'r') as file:
    instructions = file.read().split("\n")[:1][0]
with open('input8.txt', 'r') as file:
    L=[[subsub.split(", ") for subsub in sub.split(" = (")][1][0] for sub in file.read().split("\n")[2:-1]]
with open('input8.txt', 'r') as file:
    R = [[[subsubsub.split(")")[0] for subsubsub in subsub.split(", ")] for subsub in sub.split(" = (")][1][1] for sub in file.read().split("\n")[2:-1]]

multilock=[]
numbers=[]

for item in map:
    if item[2] == "A":
        multilock.append(item)
print(multilock)

for item in multilock:
    found=False
    n=0
    ii=0
    while not found:
        n += 1
        #print (f"we're at {item}")
        #print(f"takeing a {instructions[ii]}")
        if instructions[ii]=="L":
            #print(f"going to {L[map.index(item)]}")
            item = L[map.index(item)]
            if item[2] == "Z":
                numbers.append(n)
                print(n)
                found=True
        if instructions[ii]=="R":
            #print(f"going to {R[map.index(item)]}")
            item = R[map.index(item)]
            if item[2] == "Z":
                numbers.append(n)
                print(n)
                found=True
        if ii == len(instructions)-1: ii=0
        else: ii+=1
        #print(multilock)


numbers.sort(reverse=True)
i=0
multiplier=1
newi=1
for item in numbers:
    while True:
        i+=multiplier
        multiple=numbers[0]*i
        if multiple%item == 0:
            print(f"hit at {multiple} with {i} steps")
            multiplier=multiplier*i/newi
            newi=i
            break
