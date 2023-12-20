with open('input6.txt', 'r') as file:
    speedtime=[[int(subsub) for subsub in sub.split(" ") if subsub.isdigit()] for sub in file.read().split("\n")]

speedtime=[[58996469],[478223210191071],[]]
print(speedtime)
n=0
i=0
while i <= len(speedtime[0])-1:
    n = 0
    while n <= (speedtime[0][i])/2:
        if (speedtime[0][i])%2 != 0:
            presstime = ((speedtime[0][i]) / 2) + 0.5
        else:
            presstime=(speedtime[0][i])/2
        if ((presstime + n) * ((speedtime[0][i]-presstime)-n)) > speedtime[1][i]:
            n += 1
        else:
            break
    speedtime[2].append((n*2)) if (speedtime[0][i])%2 != 0 else speedtime[2].append(((n-1)*2)+1)
    i += 1
sum=1
for i in speedtime[2]:
    sum=sum*i
print(sum)