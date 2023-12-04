f = open("G:\\Github\AdventOfCode2023\Day3\Engine.txt", "r")
inp = f.read()
list = []
list.append(inp[:141])
total = 0

for i in range(0, 3, 1):
    list.append(inp[i * 141:(i + 1) * 141])

def ActualSearch(line, location):
    number = ''
    if line[location].isnumeric():
        index = 0
        while line[location + index].isnumeric():
            number = number + line[location + index]
            index += 1
        index = 1
        while line[location - index].isnumeric():
            number = line[location - index] + number
            index += 1
    elif line[location - 1].isnumeric():
        index = 1
        while line[location - index].isnumeric():
            number = line[location - index] + number
            index += 1
    elif line[location + 1].isnumeric():
        index = 0
        while line[location + index].isnumeric():
            number = number + line[location + index]
            index += 1

    if number != '' and number.isnumeric() and type(number) == str:
        return int(number)
    elif number == '':
        return 0
    else:
        return int(number)

def SearchForNumbers(location, middle):
    number = 0
    for line in list:
        if list.index(line) == middle + 1:
            number += ActualSearch(line, location)
        elif list.index(line) == middle - 1:
            number += ActualSearch(line, location)
        elif list.index(line) == middle:
            number += ActualSearch(line, location)
    return number

for line in list:
    for character in line:
        if character != '.' and not character.isnumeric() and character != '\n':
            index = line.index(character)
            number = SearchForNumbers(index, list.index(line))
            total += number
            print(total)