with open('input5.txt', 'r') as file:
    seed_list=file.read().split("\n\n")[0].split(" ")[1:]
with open('input5.txt', 'r') as file:
    dest=file.read().split("\n\n")[1:]

seed_list=[int(x) for x in seed_list]
dest=[dest.split("\n")[1:] for dest in dest]
dest=[[item.split(" ") for item in sub] for sub in dest]
dest=[[[int(item) for item in subsub] for subsub in sub] for sub in dest]

def map_decode_range(seed_list,map):
    i = 0
    x=len(seed_list)
    while i <= x-1:
        start_seed=seed_list[i]
        range = seed_list[i+1]
        match=False
        seed_min = 999999999999999999
        for soil in map:
            if start_seed >= soil[1] and start_seed < (soil[1]+soil[2]):
                match=True
                if (start_seed+range) <= (soil[1]+soil[2]):
                    seed_list[i]=start_seed+(soil[0]-soil[1])
                    break
                else:
                    new_range=(start_seed+range)-(soil[1]+soil[2])
                    new_seed=(start_seed+range)-new_range
                    range=range-new_range
                    seed_list.insert(i+2,new_seed)
                    seed_list.insert(i+3,new_range)
                    seed_list[i+1]=range
                    seed_list[i] = start_seed + (soil[0] - soil[1])
                    break
            elif soil[1] < seed_min and (soil[1]-seed_list[i]) > 0:
                    seed_min=soil[1]
        if not match:
            if range > (seed_min-start_seed):
                new_range = seed_min-start_seed
                new_seed = seed_min
                range = range - new_range
                seed_list.insert(i+2,new_seed)
                seed_list.insert(i+3,range)
                seed_list[i+1] = new_range
        i+=2
        x=len(seed_list)

for line in dest:
    map_decode_range(seed_list, line)
print(min(seed_list[::2]))