def starter(stage, position, comparison, input):
    if stage < len(stages)-1:
        dots = 0
        while dots <= len(input[0])-position-sum(stages[stage:])-len(stages[stage:])+1:
            if comparison.find(stages[stage]*"#",position+dots) > -1:
                match_spot=comparison.find(stages[stage]*"#",position+dots)
                if "#" in input[0][position+dots:match_spot]:
                    break
                elif position+dots < match_spot:
                    print("we're too far")
                    pass
                elif input[0][match_spot+stages[stage]]!="#":
                    starter(stage+1,match_spot + stages[stage] + 1,comparison[:match_spot + stages[stage]] + "." + comparison[match_spot + stages[stage] + 1:],input)
                if "#" in input[0][position+dots]:
                    print("no more room for dot")
                    break
                else:
                    dots+=1
            else:
                break
    if stage == len(stages)-1:
        print("reached last stage")
        last_starter(stage, position,comparison,input)

def last_starter(stage, position, comparison, input):
    dots = 0
    while dots <= len(input[0])-position-sum(stages[stage:])-len(stages[stage:])+1:
        if comparison.find(stages[stage]*"#",position+dots) > -1:
            match_spot = comparison.find(stages[stage] * "#", position + dots)
            if "#" in input[0][match_spot +stages[stage]:]:
                print("no bueno")
                pass
            elif position + dots < match_spot:
                print("we're too far")
                pass
            elif match_spot + stages[stage] == len(comparison):
                global count
                count += 1
            else:
                # global count
                count+=1
            if "#" in input[0][position + dots]:
                print("no more room for dot")
                break
            else:
                dots+=1
        else:
            break


final=0
n=0
with open("input12.txt", "r") as file:
    for input in file:
        n+=1
        print(n)
        # prepare the string
        input=input.split(" ")
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
        starter(0, 0, comparison, input)
        print(count)
        final+=count
print(final)