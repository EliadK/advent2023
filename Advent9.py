def nest(new,old):
    n=0
    while n<len(old)-1:
        new.append(old[n]-old[n+1])
        n+=1
    return new


sum=0
sum2=0
with open("input9.txt","r") as file:
    for line in file:
        line=[int(item) for item in line.split(" ")]
        line.reverse()
        zeroes = False
        delve = [line]
        n = 0
        newnum = 0
        newnum2=0
        while not zeroes:
            temp=[]
            temp=nest(temp,delve[n])
            delve.append(temp)
            if delve[n + 1][0] == 0:
                while n >= 0:
                    newnum += delve[n][0]
                    newnum2 = delve[n][len(delve[n]) - 1] - newnum2
                    n -= 1
                zeroes = True
            n += 1
        sum+=newnum
        sum2+=newnum2

print(sum)
print(sum2)