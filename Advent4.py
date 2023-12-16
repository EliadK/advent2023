code = 0
n = 1
card_bundle={}

with open('input4.txt', 'r') as file:
    for line in file:
        card = line.split(": ")[1]
        print(f"card is card number {n}: {card}")
        winning = card.split(" | ")[0].split( )
        losing = card.split(" | ")[1].split( )
        card_bundle.update({n:card_bundle.get(n,0)+1})
        matches = 0
        for winning_number in winning:
            if winning_number in losing:
                matches += 1
        if matches > 0:
            code += pow(2,matches-1)
        number_of_copies = 1
        while number_of_copies <= card_bundle.get(n):
            card_copy = 1
            while card_copy <= matches:
                card_bundle.update({n+card_copy:card_bundle.get(n+card_copy,0) + 1})
                card_copy += 1
            number_of_copies += 1
        n +=1

print(f"code for part a is {code}")
print("The sum of all cards copied:")
print(sum(card_bundle.values()))