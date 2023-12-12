f = open("G:\\Github\AdventOfCode2023\Day3\Engine.txt", "r")
start = f.read()
list=[]
linesData=[]
total = 0
special = ["%","@","#","*","$","/","-","+","="]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

for i in range(0, 140, 1):
    list.append(start[i * 141:(i + 1) * 141])

for line in list:
    lineT = line.replace("."," ").split()
    print(lineT)
    for element in lineT:
        if any(True for c in special) and any(True for c in numbers):
            print(element)
            for s in special:
                if s in element:
                    elements = element.split(s)
                    lineT.remove(element)
                    lineT.append(elements[0])
                    lineT.append(elements[1])
                    print(elements)
                    print(element)
    for character in lineT:
        for thing in character:
            lineData = {
                "Line": list.index(line),
                "Location": line.index(thing),
                "Character": thing,
                }
            linesData.append(lineData)

for item in linesData:
    if not item["Character"].isnumeric():
        for checkerItem in linesData:
            if checkerItem["Line"] == item["Line"] or checkerItem["Line"] == item["Line"]-1 or checkerItem["Line"] == item["Line"]+1:
                if checkerItem["Character"].isdigit():
                    if len(checkerItem["Character"])==2:
                        if checkerItem["Location"] == item["Location"]-2 or checkerItem["Location"] == item["Location"]-1 or checkerItem["Location"] == item["Location"] or checkerItem["Location"] == item["Location"]+1 or checkerItem["Location"] == item["Location"]+2:
                            total+=int(checkerItem["Character"])
                    else:
                        if checkerItem["Location"] == item["Location"]-3 or checkerItem["Location"] == item["Location"]-2 or checkerItem["Location"] == item["Location"]-1 or checkerItem["Location"] == item["Location"] or checkerItem["Location"] == item["Location"]+1 or checkerItem["Location"] == item["Location"]+2 or checkerItem["Location"] == item["Location"]+3:
                            total+=int(checkerItem["Character"])
print(total)