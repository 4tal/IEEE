sizeOfSquare=int(raw_input())
inputMatrix=[]

for line in range(sizeOfSquare):
    row=raw_input()
    inputMatrix.append([ int(element) for element in row.split()])

wrongRows=[]

diagonalSum=0
for simDiago in range(sizeOfSquare):
        diagonalSum += inputMatrix[simDiago][simDiago]

for line in range(sizeOfSquare):
    currRowSum=sum(inputMatrix[line])
    if currRowSum!=diagonalSum :
        wrongRows.append(line+1)

for column in range(sizeOfSquare):
    currColSum=0
    for row in range(sizeOfSquare):
        currColSum=inputMatrix[row][column]+currColSum
    if currColSum!=diagonalSum:
        wrongRows.append(-(column+1))

#AntiDiagonal
currRevDia=0
for sim in range(sizeOfSquare-1,-1,-1):
    currRevDia=currRevDia+inputMatrix[sizeOfSquare-sim-1][sim]

if currRevDia!=diagonalSum:
    wrongRows.append(0)

if len(wrongRows)==0:
    wrongRows.append(0)
    print wrongRows[0]
else:
    sortedWrongRowsForPrinting=sorted(wrongRows)
    print len(wrongRows)
    for errorNumber in range(len(wrongRows)):
        print sortedWrongRowsForPrinting[errorNumber]
