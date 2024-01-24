import time
t = time.process_time()

def windwipe(string1,string2):
    index=0
    found=0
    while index < len(string1) and found <= 1:
        if string1[index] != string2[index]:
            found+=1
        index+=1
    if index==len(string1):
        return True
    else:
        return False

sum = 0
sum2=0
n=0
with open("input13.txt","r") as file:
    terrain=file.read().split("\n\n")
for input in terrain:
    n+=1
    input = input.split("\n")
    index = 0
    while index <= len(input) - 2:
        endex = index + 1
        begindex=index
        smudge=0
        while begindex >= 0 and endex <= len(input) - 1 and smudge <=1:
            if input[begindex]==input[endex]:
                begindex-=1
                endex+=1
            elif windwipe(input[begindex],input[endex]):
                smudge+=1
                begindex -= 1
                endex += 1
            else:
                break
        if begindex < 0 or endex > len(input)-1:
            if smudge == 1:
                sum2+=100 * (index + 1)
            else:
                sum += 100 * (index + 1)
        index += 1

    index = 0
    while index <= len(input[0])-2:
        endex = index + 1
        begindex = index
        smudge = 0
        while begindex >= 0 and endex <= len(input[0]) - 1:
            lindex = 0
            while lindex <= len(input) - 1 and smudge <= 1:
                if input[lindex][begindex] == input[lindex][endex]:
                    lindex+=1
                else:
                    smudge+=1
                    lindex += 1
            if lindex > len(input) - 1 and smudge <=1:
                begindex -= 1
                endex += 1
                if begindex < 0 or endex > len(input[0]) - 1:
                    if smudge == 1:
                        sum2 +=index + 1
                    else:
                        sum += index + 1
                    break
            else:
                break
        index+=1

print(sum)
print(sum2)
print(time.process_time()-t)