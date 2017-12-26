def main():
    numberOfTests=int(raw_input())
    while(numberOfTests):
        parallelGames=int(raw_input())
        piles = []

        for _ in range(parallelGames):
            null=raw_input()
            piles += [int(x) for x in raw_input().split()]

        howManyTurnsNeeded = 0
        for pile in piles:
            if pile == 1:
                continue
            howManyTurnsNeeded += (pile // 2)

        if (howManyTurnsNeeded%2==0):
                print "Bob"
        else:
            print "Alice"
        numberOfTests-=1
main()
