with open("G:\\Github\\AdventOfCode2023\\Day2\\Cubes.txt", "r") as f:
    games = f.read().split("Game")[1:]

total = 0
totalPowers = 0
powerChecker = {'red': 0, 'green': 0, 'blue': 0}
powerChecker['red']=0
powerChecker['blue']=0
powerChecker['green']=0

for game in games:
    gameId = game.split(":")[0].split()[-1]
    game = game[game.find(":") + 1:]
    powerChecker['red']=0
    powerChecker['blue']=0
    powerChecker['green']=0  

    cubeCounts = {'red': 0, 'green': 0, 'blue': 0}
    allowed = True

    subsets = game.split(";")
    for subset in subsets:
        subset = subset.strip().split(",")
        for cube in subset:
            cube = cube.strip().split()
            if cube:
                number = int(cube[0])
                color = cube[1].lower().replace(',','').replace(";",'')
                cubeCounts[color] = number

                if cubeCounts['red'] > 12 or cubeCounts['green'] > 13 or cubeCounts['blue'] > 14:
                    allowed = False   
        if cubeCounts['red'] > powerChecker['red']:
            powerChecker['red'] = cubeCounts['red']
        if cubeCounts['blue'] > powerChecker['blue']:
            powerChecker['blue'] = cubeCounts['blue']
        if cubeCounts['green'] > powerChecker['green']:
            powerChecker['green'] = cubeCounts['green']        
    totalPowers += powerChecker['blue']*powerChecker['green']*powerChecker['red']

    if allowed:
        total += int(gameId)

print(f"TOTAL: {total}\nPOWERS: {totalPowers}")