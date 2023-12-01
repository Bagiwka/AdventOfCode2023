f = open("G:\\Python\AdventOfCode\Day1\Trebuchet.txt", "r")
list = f.read()
splitList = list.split() 

total = 0

def SearchForFirstNumber(word):
    for letter in word:
        if letter.isnumeric():
            break
    return(letter)

def SearchForLastNumber(word):
    for letter in word:
        if letter.isnumeric():
            lastNumber = letter
    return(lastNumber)

for word in splitList:
    firstNumber = SearchForFirstNumber(word)
    lastNumber = SearchForLastNumber(word)
    total += int(firstNumber+lastNumber)    
    print(f"Word: {word}, Numbers: {firstNumber+lastNumber}, Total: {total}")