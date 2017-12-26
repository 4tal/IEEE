def main():
    testCases = int(raw_input())
    for testCase in range(testCases):
        numberOfDogs,numberOfEmployees = [int(i) for i in raw_input().split()]

        dogsArray = []
        diffArray = []

        for dog in range(numberOfDogs):
            dogsArray.append(int(raw_input()))

        dogsArray = sorted(dogsArray)

        for elemForDiff in range(len(dogsArray)-1):
            diffArray.append(dogsArray[elemForDiff+1] - dogsArray[elemForDiff])

        diffArray = sorted(diffArray)

        minumumSum = dogsArray[numberOfDogs-1] - dogsArray[0]

        if(numberOfEmployees>1):

            for i in range(numberOfDogs-1-(numberOfEmployees-1),numberOfDogs-1):
                minumumSum-=diffArray[i]

        print(minumumSum)


main()
