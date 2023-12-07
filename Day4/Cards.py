with open("G:\\Github\\AdventOfCode2023\\Day4\\Cards.txt", "r") as f:
    cardList = f.read()

cardsData = []
output = 0

cards = cardList.split('\n')
for card in cards:
    if not card:
        continue

    cardParts = card.split('|')
    cardID = cardParts[0].split(':')[0].strip().replace("Card","").replace(" ","")
    beforePipe = cardParts[0].split(':')[1].strip()
    afterPipe = cardParts[1].strip() if len(cardParts) > 1 else None

    cardData = {
        "ID": cardID,
        "Before": beforePipe,
        "After": afterPipe,
        "Amount": 1
    }

    cardsData.append(cardData)

for card in cardsData:
    amount = 1
    for repetition in range(0, amount, 1):
        print(card)
        total = 0
        inputs = card["After"].split()
        winners = card["Before"].split()
        for number in inputs:
            for win in winners:
                if number == win:
                    total += 1          
        for i in range(1,total,1):
            for element in cardsData:
                if int(element["ID"]) == int(card["ID"])+i:
                    cardsData[cardsData.index(element)]["Amount"] += 1
        amount = cardsData[cardsData.index(element)]["Amount"]
        print(amount)
    print(total)

finalAmount = 0
for card in cardsData:
    finalAmount += card["Amount"]

print(finalAmount)
#19855