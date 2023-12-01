f = open("G:\\Github\AdventOfCode2023\Day1\Trebuchet.txt", "r")
list = f.read()
splitList = list.split() 
wordNumber = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0

def SearchForFirstNumber(word):
    for letter in word:
        if letter.isnumeric():
            break
    return letter

def SearchForFirstWord(word, firstNum):
    contained = [x for x in wordNumber if x in word]
    if contained != []:
        element = min(contained, key=word.find)
        if word.find(element) < word.find(firstNum):
            firstNum = str(wordNumber.index(element) + 1)
    return firstNum

def SearchForLastWord(word, lastNum):
    contained = [x for x in wordNumber if x in word]
    if contained != []:
        element = max(contained, key=word.rfind)
        if word.rfind(element) > word.rfind(lastNum):
            lastNum = str(wordNumber.index(element) + 1)
    return lastNum

def SearchForLastNumber(word):
    for letter in word:
        if letter.isnumeric():
            lastNumber = letter
    return(lastNumber)

for word in splitList:
    firstNumber = SearchForFirstNumber(word)
    firstNumber = SearchForFirstWord(word, firstNumber)
    lastNumber = SearchForLastNumber(word)
    lastNumber = SearchForLastWord(word, lastNumber)
    total += int(firstNumber+lastNumber)    
    print(f"Word: {word}, Numbers: {firstNumber+lastNumber}")
print(f"Total: {total}")