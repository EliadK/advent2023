# ingest input
with open("input10.txt", "r") as file:
    input = file.read()
input = [list(item) for item in input.split("\n")]

# define pipe class and type map
map = {"-": [[0, -1], [0, 1]], "J": [[0, -1], [-1, 0]], "F": [[0, 1], [1, 0]], "7": [[0, -1], [1, 0]],
       "L": [[0, 1], [-1, 0]], "|": [[-1, 0], [1, 0]], "S": [[0, 0], [0, 0]], ".": [[0, 0], [0, 0]]}


class pipe:
    def __init__(self, coords):
        self.type = input[coords[0]][coords[1]]
        self.coords = coords

    def __str__(self):
        return f"{self.coords},{self.type}"

    def isconnected(self, coords):
        connector1 = [self.coords[0] + map[self.type][0][0], self.coords[1] + map[self.type][0][1]]
        connector2 = [self.coords[0] + map[self.type][1][0], self.coords[1] + map[self.type][1][1]]
        if self.type != "S":
            if connector1 == coords or connector2 == coords:
                return True

    def move(self, coords):
        connector1 = [self.coords[0] + map[self.type][0][0], self.coords[1] + map[self.type][0][1]]
        connector2 = [self.coords[0] + map[self.type][1][0], self.coords[1] + map[self.type][1][1]]
        if connector1 == coords:
            print(f"going to {connector2}")
            return connector2
        if connector2 == coords:
            print(f"going to {connector1}")
            return connector1


# find start point
start = [0, 0]
# coords are [line,spot]
for i in input:
    if i.count("S") == 1:
        start[0] = input.index(i)
        start[1] = i.index("S")

destination1 = pipe(start)
destination2 = pipe([0, 0])

# find first connection to start point
l = -1
s = -1
while l <= 1:
    s = -1
    while s <= 1 and not destination2.isconnected(start):
        print(f"checking {start[0] + l},{start[1] + s}")
        destination2 = pipe([start[0] + l, start[1] + s])
        s += 1
    l += 1
print(f"connection found it at {destination2}")

# add surface area calculation
surface = [0, 0]
surface[1] += (destination2.coords[1] - destination1.coords[1])
surface[0] += (destination2.coords[0] - destination1.coords[0]) * (surface[1])

# begin movement out of "start"
destination1 = pipe(destination2.move(destination1.coords))
surface[1] += (destination1.coords[1] - destination2.coords[1])
surface[0] += (destination1.coords[0] - destination2.coords[0]) * (surface[1])

# continue movement until back to start
n = 1
while destination2.coords != start and destination1.coords != start:
    n += 1
    destination2 = pipe(destination1.move(destination2.coords))
    surface[1] += (destination2.coords[1] - destination1.coords[1])
    surface[0] += (destination2.coords[0] - destination1.coords[0]) * (surface[1])
    destination1 = pipe(destination2.move(destination1.coords))
    surface[1] += (destination1.coords[1] - destination2.coords[1])
    surface[0] += (destination1.coords[0] - destination2.coords[0]) * (surface[1])

print(f"Pipe length is {n}")
print(f"The area trapped within the pipe is {abs(surface[0]) - n + 1}")
