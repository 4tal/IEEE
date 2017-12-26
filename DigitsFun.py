def main():
    inputString=raw_input()
    while(inputString != ("END")):
        print lowestEqualness(inputString)
        inputString=raw_input()

def lowestEqualness(inputString):
    counter=1
    while(len(inputString)!=int(inputString)):
        inputString=str(len(inputString))
        counter+=1
    return counter

main()
