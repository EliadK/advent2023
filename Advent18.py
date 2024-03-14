import time
t=time.process_time()

with open("input18.txt") as file:
    digplan=file.read()

digplan=[[attribute.strip("()") for attribute in line.split(" ")] for line in digplan.strip().split("\n")]
sum=1
dig=0
ditchsum=0
for line in digplan:
    direct,count,color=line
    count=int(count)
    ditchsum+=count
    match direct:
        case "R":
            dig+=count
            sum-=count
        case "L":
            dig-=count
        case "U":
            sum-=count*dig
            sum -= count
        case "D":
            sum+=count*dig
print(sum+ditchsum)
directmap={"0":"R","1":"D","2":"L","3":"U"}
sum=1
dig=0
ditchsum=0
for line in digplan:
    count=int(line[2][1:-1],16)
    direct=directmap[line[2][-1:]]
    ditchsum+=count
    match direct:
        case "R":
            dig+=count
            sum-=count
        case "L":
            dig-=count
        case "U":
            sum-=count*dig
            sum -= count
        case "D":
            sum+=count*dig
print(sum+ditchsum)
print(time.process_time()-t)