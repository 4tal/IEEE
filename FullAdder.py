base, chars=raw_input().split()

charsList=list(chars)
numbers=range(0,int(base))

letToNum={}
numToLet={}

for i in range(0,int(base)):
    letToNum[charsList[i]]=i
    numToLet[i]=charsList[i]

#x=list(raw_input())
x=list(''.join([j for j in raw_input() if j in chars]))

#y=list(raw_input())
y=list(''.join([z for z in raw_input() if z in chars]))

g1=raw_input()
g2=raw_input()

x=x[::-1]
y=y[::-1]

result=[]
counter=0
carryNum=0

while(counter<len(x) or counter<len(y)):
    if(counter>=len(x)):
        counterX=0
    else:
        counterX=int(letToNum[x[counter]])
    if(counter>=len(y)):
        counterY=0
    else:
        counterY=int(letToNum[y[counter]])


    sum=counterX+counterY+carryNum
    if(sum<=(int(base)-1)):
        carryNum=0
    else:
        carryNum=1
    sum=sum%int(base)
    result.append(numToLet[sum])
    counter+=1



print "".join(base),"".join(chars)
print (max(len(x),len(y))-len(x)+1)*" "+"".join(x[::-1])
print "+"+(max(len(x),len(y))-len(y))*" "+"".join(y[::-1])
print "-"*(max(len(x),len(y))+1)
print " "*(max(len(x),len(y))-len(result)+1)+"".join(result[::-1])
