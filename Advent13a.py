import time
t = time.process_time()
sum = 0
n=0
with open("input13.txt","r") as file:
    terrain=file.read().split("\n\n")
for input in terrain:
    input = input.split("\n")
    index = 0
    while index <= len(input) - 2:
        endex = index + 1
        begindex=index
        while begindex >= 0 and endex <= len(input) - 1:
            if input[begindex]==input[endex]:
                begindex-=1
                endex+=1
            else:
                break
        if begindex < 0 or endex > len(input)-1:
            sum += 100 * (index + 1)
        index += 1

    index = 0
    while index <= len(input[0])-2:
        endex = index + 1
        begindex = index
        while begindex >= 0 and endex <= len(input[0]) - 1:
            lindex = 0
            while lindex <= len(input) - 1:
                if input[lindex][begindex] == input[lindex][endex]:
                    lindex+=1
                else:
                    break
            if lindex > len(input) - 1:
                begindex -= 1
                endex += 1
                if begindex < 0 or endex > len(input[0]) - 1:
                    sum += index + 1
                    break
            else:
                break
        index+=1

print(sum)
print(time.process_time()-t)