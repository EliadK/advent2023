with open('input5.txt', 'r') as file:
    seed_list=file.read().split("\n\n")[0].split(" ")[1:]
with open('input5.txt', 'r') as file:
    dest=file.read().split("\n\n")[1:]

dest=[dest.split("\n")[1:] for dest in dest]
dest=[[item.split(" ") for item in sub] for sub in dest]

def map_decode(seed,map):
    for soil in map:
        min=soil[1]
        max=int(soil[1])+int(soil[2])
        if int(seed) >= int(min) and int(seed) <= max:
            difference=int(soil[0])-int(soil[1])
            seed=int(seed)+difference
            return seed
    return int(seed)

for line in dest:
    seed_list = [map_decode(seed, line) for seed in seed_list]
print(min(seed_list))