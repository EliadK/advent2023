import time
t=time.process_time()
with open("input15.txt","r") as file:
    input=file.read()[:-1]

input="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
input=input.split(",")
val=0
sum=0
def hash(current_value,character):
    return ((ord(character)+current_value)*17)%256

def full_hash(current_value,string):
    new_value=current_value
    for character in string:
        new_value=hash(new_value,character)
    return new_value

for cell in input:
    sum+=full_hash(val,cell)
print(sum)
print(t-time.process_time())