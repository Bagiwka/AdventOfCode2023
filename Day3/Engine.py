f = open("G:\\Github\AdventOfCode2023\Day3\Engine.txt", "r")
inp = f.read()
list = []
total = 0

for i in range(0, 140, 1):
    list.append(inp[i * 141:(i + 1) * 141])

def ActualSearch(line, location, again):
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
    elif line[location+1].isnumeric() and again == False:
        index = 1
        while line[location + index].isnumeric():
            number = number + line[location + index]
            index += 1
            again = True
    elif line[location-1].isnumeric():
        index = 1
        while line[location - index].isnumeric():
            number = line[location - index] + number
            index += 1
            again = False
    print(line[location-1],line[location-1+1],line[location+1])

    if number != '' and number.isnumeric() and type(number) == str:
        return int(number), again
    elif number == '':
        return 0, again
    else:
        return int(number), again

def SearchForNumbers(location, middle, again):
    number = 0
    numRem = 0
    for i, line in enumerate(list):
        if i == middle + 1:
            numRem = number
            number, again = ActualSearch(line, location, again)
            number = numRem + number
        if i == middle:
            numRem = number
            number, again = ActualSearch(line, location, again)
            number = numRem + number
        if i == middle - 1:
            numRem = number
            number, again = ActualSearch(line, location, again)
            number = numRem + number
    return number, again


for line in list:
    print("INDEX: ", list.index(line), 'LINE: ', line)
    index = 0
    for character in line:
        again = False
        if character != '.' and not character.isnumeric() and character != '\n':
            number, again = SearchForNumbers(index, list.index(line), again)
            if again:
                total += number
                print("TOTAL: ", total)
                print("CHAR: ", character)
                print("NUM: ", number, "\n")
                number, again = SearchForNumbers(index, list.index(line), again)
                total += number
                print("TOTAL: ", total)
                print("CHAR: ", character)
                print("NUM: ", number, "\n")
            else:
                total += number
                print("TOTAL: ", total)
                print("CHAR: ", character)
                print("NUM: ", number, "\n")
        index += 1
print(f"FINISHED\nTOTAL: {total}")