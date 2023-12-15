# load each line, look for highest number + r/b/g. look for red, go back two index spots
# compare with r/b/g max
# if pass then solution += n
# increase n += 1

solution=0
n=1
color_limit={"red":12,"green":13,"blue":14}
with open('input2.txt', 'r') as file:
    for line in file:
        print(line)
        fucked=False
        print(f"Strating game {n}")
        for color in color_limit.keys():
            print(color)
            i=0
            while i != -1:
                compare = int(line[(line.find(color) - 3):(line.find(color) - 1)])
                line = line.replace(color, "xxx", 1)
                print(compare)
                if compare > color_limit[color]:
                    print("fuck")
                    if not fucked:
                        solution -= n
                        print("Fuck noted")
                    fucked=True
                i = line.find(color)
        solution += n
        n += 1
        print(f"code is {solution}")
        print(f"Moving to game {n}")


