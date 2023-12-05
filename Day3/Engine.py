f = open("G:\\Github\AdventOfCode2023\Day3\Engine.txt", "r")
inp = f.read()
list = []
total = 0

for i in range(0, 3, 1):
    list.append(inp[i * 141:(i + 1) * 141])

def ActualSearch(line, location):
    number = ''
    
    if line[location].isnumeric():
        index = 0
        add=0
        while line[location + index].isnumeric():
            number = number + line[location + index]
            index += 1
            add=1
        index = 0+add
        while line[location - index].isnumeric():
            number = line[location - index] + number
            index += 1
    elif line[location+1].isnumeric():
        index = 0
        while line[location + index].isnumeric():
            number = number + line[location + index]
            index += 1
    elif line[location-1].isnumeric():
        index = 1
        while line[location - index].isnumeric():
            number = line[location - index] + number
            index += 1

    if number != '' and number.isnumeric() and type(number) == str:
        return int(number)
    elif number == '':
        return 0
    else:
        return int(number)

def SearchForNumbers(location, middle):
    number = 0
    for i, line in enumerate(list):
        if i == middle + 1 or i == middle - 1 or i == middle:
            number += ActualSearch(line, location)
    return number


for line in list:
    print("INDEX: ", list.index(line), 'LINE: ', line)
    index = 0
    for character in line:
        if character != '.' and not character.isnumeric() and character != '\n':
            number = SearchForNumbers(index, list.index(line))
            total += number
            print("TOTAL: ", total)
            print("CHAR: ", character)
            print("NUM: ", number, "\n")
        index += 1