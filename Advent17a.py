import time
t=time.process_time()

with open("input17.txt") as file:
    heatmap=file.read()

heatmap="""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

heatmap=heatmap.split("\n")
row_limit=len(heatmap)
cul_limit=len(heatmap[0])

heatmap={(y, x): [int(v),10000,0,"direction",0] for y,row in enumerate(heatmap)
         for x,v in enumerate(row)}

def opened_sort(key):
    value,weight,distance,direction,direction_steps=key[1]
    return weight+distance


def calc_distance(pos):
    x,y=pos
    endx,endy=end
    return abs(x-endx)+abs(y-endy)


directions={"down":(1,0),"right":(0,1),"up":(-1,0),"left":(0,-1)}


opened=[]
closed=[]
start=(0,0)
end=(row_limit-1,cul_limit-1)
mindist=1000

for pos in heatmap:
    heatmap[pos][2]=calc_distance(pos)

heatmap[start][1]=0
opened.append([start,heatmap[start]])

while opened:
    opened.sort(key=opened_sort,reverse=True)
    pos, values = opened.pop()
    y,x=pos
    value, sum_dist, distance, direction, direction_steps =values
    closed.append(pos)
    if pos == end:
        if sum_dist < mindist:
            mindist=sum_dist
    for heading,coords in directions.items():
        ydel,xdel=coords
        newpos=(y+ydel,x+xdel)
        if newpos in closed or newpos not in heatmap.keys():
            continue
        newvalues=heatmap[newpos].copy()
        if direction == heading:
            if direction_steps >= 2:
                continue
            else:
                newvalues[4]=direction_steps+1
                newvalues[3] = heading
        else:
            newvalues[4]=0
            newvalues[3] = heading
        if [newpos,newvalues] in opened:
            old_distance = opened.remove([newpos, newvalues])
            if old_distance[1][2] > newvalues[0] + sum_dist:
                newvalues[1] = newvalues[0] + sum_dist
                opened.append([newpos, newvalues])
            else:
                opened.append(old_distance)
        else:
            newvalues[1] = newvalues[0] + sum_dist
            opened.append([newpos, newvalues])

print(mindist)
print(time.process_time()-t)