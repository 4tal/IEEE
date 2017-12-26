def getRepresent(width,height):
    currLet = input()
    structureOfTheLetter = []
    for lineInRepresentaion in range(height):
        partOfLetter = input()
        partOfLetter = partOfLetter.ljust(width)
        structureOfTheLetter.append(partOfLetter)
    return currLet,structureOfTheLetter

def main():
    width = int(input())
    height = int(input())
    howManyLetters = int(input())

    abDictionary = {}

    while(howManyLetters):
        res=getRepresent(width,height)
        abDictionary[res[0]]=res[1]
        howManyLetters-=1


    howManyStringsToShow = int(input())
    stringsToShow = []
    while(howManyStringsToShow):
        stringsToShow.append(input())
        howManyStringsToShow-=1

    for string in stringsToShow:
        for line in range(height):
            for char in string:
                print (abDictionary[char][line],end="")
            print()

main()
