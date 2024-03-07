import time
import heapq
t=time.process_time()

with open("input17.txt") as file:
    heatmap=file.read()

heatmap=heatmap.split("\n")
row_limit=len(heatmap)
cul_limit=len(heatmap[0])

# take heatmap and turn it into dictionary (r,c)=weight using dict compreh
heatmap={(y, x): int(v) for y,row in enumerate(heatmap)
         for x,v in enumerate(row)}

directions={"down":(1,0),"right":(0,1),"up":(-1,0),"left":(0,-1)}
opened=[[0,0,0,"dir",4]]
closed=set()
poscost={}
end=(row_limit-1,cul_limit-1)

while opened:
    sum_dist, y,x, direction, direction_steps = heapq.heappop(opened)
    pos=(y,x)
    keypos=(pos,direction,direction_steps)
    closed.add(keypos)
    if pos == end:
        print(sum_dist)
        break
    for heading,(ydel,xdel) in directions.items():
        newpos=(y+ydel,x+xdel)
        if newpos not in heatmap.keys():
            continue
        if direction != heading and direction_steps < 4:
            continue
        elif (direction == "up" and heading == "down") or (direction == "down" and heading == "up") or (direction == "right" and heading == "left") or (direction == "left" and heading == "right"):
            continue
        elif direction == heading:
            if direction_steps == 10:
                continue
            else:
                newdirection_steps = direction_steps+1
                newdirection = heading
        else:
            newdirection_steps = 1
            newdirection = heading
        newkeypos = (newpos, newdirection, newdirection_steps)
        if newkeypos in closed:
            continue
        value=heatmap[newpos]
        newy, newx = newpos
        new_sum = value + sum_dist
        if newkeypos not in poscost.keys():
            heapq.heappush(opened, [new_sum, newy, newx, newdirection, newdirection_steps])
            poscost[newkeypos] = new_sum
        else:
            if poscost[newkeypos] > new_sum:
                old_sum=poscost[newkeypos]
                opened[opened.index([old_sum, newy, newx, newdirection, newdirection_steps])]=[new_sum, newy, newx, newdirection, newdirection_steps]
                poscost[newkeypos]=new_sum
print(time.process_time()-t)