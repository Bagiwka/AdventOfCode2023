f = open("G:\\Github\AdventOfCode2023\Day3\Engine.txt", "r")
start = f.read()
list=[]
linesData=[]
total = 0

for i in range(0, 140, 1):
    list.append(start[i * 141:(i + 1) * 141])

for line in list:
    lineT = line.replace("."," ").split()
    id=0
    for character in lineT:
        for element in character:
            if not element.isdigit or element == '%'or element == '*':
                linetemp=character.split(element)
                break
            else:
                linetemp=[character]
        for thing in linetemp:
            lineData = {
                "Line": list.index(line),
                "ID": id,
                "Location": line.index(thing),
                "Character": thing,
                }
            id+=1
            linesData.append(lineData)

for item in linesData:
    if not item["Character"].isnumeric():
        for checkerItem in linesData:
            if checkerItem["Line"] == item["Line"] or checkerItem["Line"] == item["Line"]-1 or checkerItem["Line"] == item["Line"]+1:
                if checkerItem["Character"].isdigit():
                    if len(checkerItem["Character"])==2:
                        if checkerItem["Location"] == item["Location"]-2 or checkerItem["Location"] == item["Location"]-1 or checkerItem["Location"] == item["Location"] or checkerItem["Location"] == item["Location"]+1 or checkerItem["Location"] == item["Location"]+2:
                            total+=checkerItem["Location"]
                            print(checkerItem)
                    else:
                        if checkerItem["Location"] == item["Location"]-3 or checkerItem["Location"] == item["Location"]-2 or checkerItem["Location"] == item["Location"]-1 or checkerItem["Location"] == item["Location"] or checkerItem["Location"] == item["Location"]+1 or checkerItem["Location"] == item["Location"]+2 or checkerItem["Location"] == item["Location"]+3:
                            total+=checkerItem["Location"]
                            print(checkerItem)
print(total)