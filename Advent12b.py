cache={}
def starter(stage, comparison):
    position=len(input[0])-len(comparison)
    key=tuple(stages[stage:]),tuple(input[0][position:])
    if key in cache:
        return cache[key]
    i = 0
    match_spot = comparison.find(stages[stage] * "#")
    if match_spot > -1 and len(comparison) >= sum(stages[stage:]) + len(stages[stage:])-1:
        if match_spot > 0:
            if "#" in input[0][position:position+match_spot]:
                return 0
            else:
                return starter(stage, comparison[match_spot:])
        else:
            if stage == len(stages) - 1:
                if "#" not in input[0][position+stages[stage]:]:
                    i += 1
            else:
                if "#" not in input[0][position + stages[stage]]:
                    i+= starter(stage+1,comparison[stages[stage]+1:])
            if "." in input[0][position] or "?" in input[0][position]:
                if len(comparison)-1 >= sum(stages[stage:]) + len(stages[stage:])-1:
                    i += starter(stage, comparison[1:])
        cache[key]=i
        return i
    else:
        return 0

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
        count+=starter(0, comparison)
        print(count)
        final+=count
print(final)
print(time.process_time() - t)