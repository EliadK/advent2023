import time
t=time.process_time()

with open("input19.txt") as file:
    partsplan=file.read()

workflows,parts=partsplan.strip().split("\n\n")

workflows={line.split("{")[0]:line.strip("}").split("{")[1].split(",") for line in workflows.split("\n")}

parts=[[int(attribute[2:]) for attribute in part.strip("{}").split(",")] for part in parts.split("\n")]


def start_workflow(workflow):
    x,m,a,s=part
    for condition in workflows[workflow][:-1]:
        term,result=condition.split(":",1)
        if eval(term):
            match result:
                case "A":
                    return "A"
                case "R":
                    return "R"
                case x:
                    return start_workflow(x)
    match workflows[workflow][-1]:
            case "A":
                return "A"
            case "R":
                return "R"
            case x:
                return start_workflow(x)


def range_workflows(workflow):
    global newsum
    global part
    original_part={key:value.copy() for key, value in part.copy().items()}
    for condition in workflows[workflow][:-1]:
        term, result = condition.split(":", 1)
        category=term[0]
        modifier=term[1]
        range=int(term[2:])
        match modifier:
            case "<":
                if part[category][1] >= range > part[category][0]:
                    oldrange = part[category][1]
                    part[category][1]=range-1
                    match result:
                        case "A":
                            subsum = 1
                            for x in part.values():
                                subsum=subsum*(x[1]-x[0]+1)
                            newsum += subsum
                        case "R":
                            pass
                        case x:
                            range_workflows(x)
                    part[category][1] = oldrange
                    part[category][0] = range
            case ">":
                if part[category][0] <= range < part[category][1]:
                    oldrange=part[category][0]
                    part[category][0]=range+1
                    match result:
                        case "A":
                            subsum = 1
                            for x in part.values():
                                subsum=subsum*(x[1]-x[0]+1)
                            newsum+= subsum
                        case "R":
                            pass
                        case x:
                            range_workflows(x)
                    part[category][0] = oldrange
                    part[category][1] = range
    match workflows[workflow][-1]:
        case "A":
            subsum = 1
            for x in part.values():
                subsum = subsum * (x[1]-x[0]+1)
            newsum += subsum
        case "R":
            pass
        case x:
            range_workflows(x)
    part = original_part

sums=0
for part in parts:
    if start_workflow("in")=="A":
        sums+=sum(part)

part={"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]}
newsum=0
range_workflows("in")
print(sums)
print(newsum)
print(time.process_time()-t)