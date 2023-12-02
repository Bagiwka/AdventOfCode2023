f = open("G:\\Github\AdventOfCode2023\Day2\Cubes.txt", "r")
opened = f.read()
games=[]
list = []
i = 1
counter=0
redCounter = 0
blueCounter = 0
greenCounter = 0


for i in range(1,95):
    mid = opened[i:].find("Game")
    list.append(opened[:mid+i])
    opened = opened[mid+i:]
    i += 1


for game in list:
    colon = game.find(":")
    findGame = game.find(" ")
    id=game[findGame:colon].replace(" ",'')
    games.append(id)
    counter+=1


for game in list:
    while redCounter < len(games):
        mid = game.find("red")
        games[redCounter] = games[redCounter] +' '+ (game[mid:game.find("red")])
        game = game[mid+redCounter:]
        redCounter += 1
print(games)