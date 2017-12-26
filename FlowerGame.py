import math

def newPow(x,y):
    if(y==0):
        return 1
    else:
        return x**y


def findLevel(x):
    level=0
    while(level<67):
        if(newPow(2,level)>x):
        #if(math.pow(2,level)>x):
            return (level-1)
        level=level+1
    return level


def main():
    numberOfTests=int(raw_input())
    while(numberOfTests):
        currInput=int(raw_input())
        #game=list(range(0,currInput))
        #print findLevel(currInput)
        print int(((currInput-newPow(2,findLevel(currInput)))*2)+1)
        #print int(((currInput-(math.pow(2,findLevel(currInput))))*2)+1)
        numberOfTests-=1


main()
