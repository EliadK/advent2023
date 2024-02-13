import time
t=time.process_time()
import sys
sys.setrecursionlimit(1500000)

with open("input16.txt") as file:
    contraption=file.read()

contraption=[list(line) for line in contraption.split("\n")]
last_energized=0


def right(map,x,y):
    global energized
    if 0 <= x < len(map[0]) and 0 <= y < len(map):
        global last_energized
        if energized[y][x] == "#":
            if last_energized<2000:
                last_energized += 1
            else:
                return
        else:
            last_energized = 0
        match map[y][x]:
            case ".":
                energized[y][x] = "#"
                right(map, x + 1, y)
            case "-":
                energized[y][x] = "#"
                right(map, x + 1, y)
            case r"|":
                if energized[y][x]=="#":
                    return
                else:
                    energized[y][x]="#"
                    up(map,x,y-1)
                    down(map,x,y+1)
            case "\\":
                energized[y][x] = "#"
                down(map, x, y + 1)
            case r"/":
                energized[y][x] = "#"
                up(map, x, y - 1)

def left(map,x, y):
    global energized
    if 0 <= x < len(map[0]) and 0 <= y < len(map):
        global last_energized
        if energized[y][x] == "#":
            if last_energized<2000:
                last_energized += 1
            else:
                return
        else:
            last_energized = 0
        match map[y][x]:
            case ".":
                energized[y][x]="#"
                left(map,x - 1, y)
            case "-":
                energized[y][x] = "#"
                left(map,x - 1, y)
            case "|":
                if energized[y][x]=="#":
                    return
                else:
                    energized[y][x]="#"
                    up(map,x,y-1)
                    down(map,x,y+1)
            case "\\":
                energized[y][x]="#"
                up(map,x,y-1)
            case r"/":
                energized[y][x]="#"
                down(map,x, y + 1)


def up(map,x, y):
    global energized
    if 0 <= x < len(map[0]) and 0 <= y < len(map):
        global last_energized
        if energized[y][x] == "#":
            if last_energized<2000:
                last_energized += 1
            else:
                return
        else:
            last_energized = 0
        match map[y][x]:
            case ".":
                energized[y][x]="#"
                up(map,x, y-1)
            case "#" | "|":
                energized[y][x] = "#"
                up(map,x, y-1)
            case "-":
                if energized[y][x]=="#":
                    return
                else:
                    energized[y][x] = "#"
                    right(map, x + 1, y)
                    left(map, x - 1, y)
            case "\\":
                energized[y][x]="#"
                left(map,x-1, y)
            case r"/":
                energized[y][x]="#"
                right(map,x+1, y)

def down(map,x, y):
    global energized
    if 0 <= x < len(map[0]) and 0 <= y < len(map):
        global last_energized
        if energized[y][x] == "#":
            if last_energized<2000:
                last_energized += 1
            else:
                return
        else:
            last_energized = 0
        match map[y][x]:
            case ".":
                energized[y][x]="#"
                down(map,x, y+1)
            case "|":
                energized[y][x] = "#"
                down(map,x, y+1)
            case "-":
                if energized[y][x]=="#":
                    return
                else:
                    energized[y][x] = "#"
                    right(map, x + 1, y)
                    left(map, x - 1, y)
            case "\\":
                energized[y][x]="#"
                right(map,x+1, y)
            case r"/":
                energized[y][x]="#"
                left(map,x-1, y)

ultimate_sum=0
for i in range(len(contraption[0])):
    energized = [item.copy() for item in contraption]
    down(contraption,i,0)
    sum=0
    for line in energized:
        sum+=line.count("#")
    if sum>ultimate_sum: ultimate_sum=sum

for i in range(len(contraption[0])):
    energized = [item.copy() for item in contraption]
    up(contraption,i,len(contraption)-1)
    sum=0
    for line in energized:
        sum+=line.count("#")
    if sum>ultimate_sum: ultimate_sum=sum

for i in range(len(contraption)):
    energized = [item.copy() for item in contraption]
    right(contraption,0,i)
    sum=0
    for line in energized:
        sum+=line.count("#")
    if sum>ultimate_sum: ultimate_sum=sum

for i in range(len(contraption)):
    energized = [item.copy() for item in contraption]
    left(contraption,len(contraption[0])-1,i)
    sum=0
    for line in energized:
        sum+=line.count("#")
    if sum>ultimate_sum: ultimate_sum=sum

print(f"ultimate sum is {ultimate_sum}")
print(time.process_time()-t)
