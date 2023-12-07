with open("G:\\Github\\AdventOfCode2023\\Day4\\Cards.txt", "r") as f:
    cardList = f.read()

cardsData = []
output = 0

cards = cardList.split('\n')
for card in cards:
    if not card:
        continue

    cardParts = card.split('|')
    cardID = cardParts[0].split(':')[0].strip()
    beforePipe = cardParts[0].split(':')[1].strip()
    afterPipe = cardParts[1].strip() if len(cardParts) > 1 else None

    cardData = {
        "ID": cardID,
        "Before": beforePipe,
        "After": afterPipe
    }

    cardsData.append(cardData)

for card in cardsData:
    total = []
    inputs = card["After"].split()
    winners = card["Before"].split()
    for number in inputs:
        for win in winners:
            if number == win:
                total.append(number)
    if total != []:
        output += 2 ** (len(total)-1)
        print(output)
        print(total)