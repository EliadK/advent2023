with open('input7.txt', 'r') as file:
    cards=[sub.split(" ") for sub in file.read().split("\n")[:-1]]

suits=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
fives=[]
fours=[]
fulls=[]
threes=[]
pairs=[]
twos=[]
dreck=[]

def sorter(fours):
    for four in fours:
        four[0]=four[0].replace("T","B")
        four[0]=four[0].replace("J","C")
        four[0]=four[0].replace("Q","D")
        four[0]=four[0].replace("K","E")
        four[0]=four[0].replace("A","F")
    fours.sort()
    for four in fours:
        four[0]=four[0].replace("B","T")
        four[0]=four[0].replace("C","J")
        four[0]=four[0].replace("D","Q")
        four[0]=four[0].replace("E","K")
        four[0]=four[0].replace("F","A")

sorter(cards)

n=0
while cards:
    found = False
    for suit in suits:
        if cards[n][0].count(suit) == 5:
            fives.append(cards[n])
            cards.pop(n)
            found=True
            break
    if not found:
        for suit in suits:
            if cards[n][0].count(suit) == 4:
                fours.append(cards[n])
                cards.pop(n)
                found=True
                break
    if not found:
        for suit in suits:
            if cards[n][0].count(suit) == 3:
                double=False
                for suit_again in suits:
                    if cards[n][0].count(suit_again[0]) == 2 and suit_again[0] != suit:
                        fulls.append(cards[n])
                        cards.pop(n)
                        found = True
                        double=True
                        break
                if not double:
                    threes.append(cards[n])
                    cards.pop(n)
                    found = True
                    break
    if not found:
        for suit in suits:
            if cards[n][0].count(suit) == 2 and not found:
                double=False
                for suit_again in suits:
                    if cards[n][0].count(suit_again[0]) == 2 and suit_again[0] != suit:
                        pairs.append(cards[n])
                        cards.pop(n)
                        found = True
                        double=True
                        break
                if not double:
                    twos.append(cards[n])
                    cards.pop(n)
                    found = True
                    break
    if not found:
        dreck.append(cards[n])
        cards.pop(n)

dreck.extend(twos)
dreck.extend(pairs)
dreck.extend(threes)
dreck.extend(fulls)
dreck.extend(fours)
dreck.extend(fives)
n=1
sum=0
while n <= 1000:
    sum=sum+(int((dreck[n-1][1]))*n)
    n+=1
print(sum)