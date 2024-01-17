cache={}
def starter(stage, position, comparison):
    key=tuple(stages[stage:]),tuple(input[0][position:])
    if key in cache:
        return cache[key]
    i=0
    if stage < len(stages)-1:
        dots = 0
        while comparison.find(stages[stage]*"#",position+dots) <= len(input[0])-(sum(stages[stage:])+len(stages[stage:])-1):
            if comparison.find(stages[stage]*"#",position+dots) > -1:
                match_spot=comparison.find(stages[stage]*"#",position+dots)
                if "#" in input[0][position:match_spot]:
                    cache[key] = i+0
                    return i+0
                if position+dots < match_spot:
                    dots = match_spot - position
                if input[0][match_spot+stages[stage]]!="#":
                    i+=starter(stage+1,match_spot + stages[stage] + 1,comparison[:match_spot + stages[stage]] + "." + comparison[match_spot + stages[stage] + 1:])
                if "#" in input[0][position+dots]:
                    cache[key] = i + 0
                    return i+0
                else:
                    dots+=1
            else:
                cache[key] = i + 0
                return i+0
    if stage == len(stages)-1:
        if comparison.find(stages[stage] * "#", position) == -1:
            cache[key] = i + 0
            return i+0
        else:
            i+= last_starter(stage, position,comparison)
    cache[key] = i
    return i

def last_starter(stage, position, comparison):
    key=tuple(stages[stage:]),tuple(input[0][position:])
    if key in cache:
        return cache[key]
    i=0
    dots = 0
    while comparison.find(stages[stage]*"#",position+dots) <= len(input[0])-(sum(stages[stage:])+len(stages[stage:])-1):
        if comparison.find(stages[stage]*"#",position+dots) > -1:
            match_spot = comparison.find(stages[stage] * "#", position + dots)
            if "#" in input[0][position:match_spot]:
                cache[key] = i + 0
                return i+0
            if "#" in input[0][match_spot + stages[stage]:]:
                if "#" in input[0][position + dots]:
                    cache[key] = i + 0
                    return i+0
                else:
                    dots += 1
                    continue
            if position + dots < match_spot:
                dots = match_spot - position
            if match_spot + stages[stage] == len(comparison):
                i += 1
            else:
                i+=1
            if "#" in input[0][position + dots]:
                cache[key] = i + 0
                return i+0
            else:
                dots+=1
        else:
            break
    cache[key] = i
    return i

import time
t = time.process_time()
final=0
n=0
with open("input12.txt", "r") as file:
    for input in file:
        n+=1
        print(n)
        # prepare the string
        input=input.split(" ")
        input[1] = ((input[1] + ",") * 5)[:-1]
        input[0] = ((input[0] + "?") * 5)[:-1]
        input[1]=[int(item) for item in input[1].split(",")]
        stages=input[1]
        #split ?
        input[0]= [item for item in input[0]]
        #remove excess dots
        index=0
        while index < len(input[0])-1:
            if input[0][0] == ".":
                input[0].pop(0)
                index-=1
            elif input[0][len(input[0])-1] == ".":
                input[0].pop()
                index -= 1
            if input[0][index] == "." and input[0][index+1] == ".":
                input[0].pop(index)
                index-=1
            index+=1
        #create a comparison string with #s
        comparison=[item.replace("?","#") for item in input[0]]
        comparison="".join(comparison) # create one big # string for easy searches
        # now we need to iterate over the comparison string, while keeping original in mind
        count=0
        count+=starter(0,0, comparison)
        print(count)
        final+=count
print(final)
print(time.process_time() - t)