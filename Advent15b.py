import time
t=time.process_time()
with open("input15.txt","r") as file:
    input=file.read()[:-1]

# input="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
input=input.split(",")
lens_map=[]
for i in range(256):
    lens_map.append([])
val=0
sum=0


def hash(current_value,character):
    return ((ord(character)+current_value)*17)%256


def full_hash(current_value,string):
    box=current_value
    for character in string:
        if character not in "-=":
            box=hash(box, character)
        else:
            lens=string[-1]
            break
    if lens=="-":
        label=string[:-1]
    else:
        label=string[:-2]
    return box,label,lens


class cell:
    def __init__(self, instruction):
        self.box=instruction[0]
        self.label=instruction[1]
        self.lens=instruction[2]

    def __str__(self):
        return f"{self.label}"


for instruction in input:
    instruction=cell(full_hash(val, instruction))
    if instruction.lens=="-":
        if len(lens_map[instruction.box]) >0:
            for i in lens_map[instruction.box]:
                if i.label == instruction.label:
                    lens_map[instruction.box].remove(i)
    else:
        found=False
        if len(lens_map[instruction.box]) > 0:
            for j in lens_map[instruction.box]:
                if j.label == instruction.label:
                    j.lens = instruction.lens
                    found=True
                    break
        if not found:
            lens_map[instruction.box].append(instruction)

i=0
while i < len(lens_map):
    j=0
    while j < len(lens_map[i]):
        sum+=(1+i)*(1+j)*(int(lens_map[i][j].lens))
        j+=1
    i+=1
print(sum)
print(time.process_time()-t)