import math;

def getPage(addressOfPage,sizeOfPage):
        return (math.floor(addressOfPage/sizeOfPage));

def main():
    numberOfTests=int(input());

    for test in range(numberOfTests):
        newList = input().split(' ');
        newList=list(map(lambda x: int(x),newList))
        numberOfPagesPerProcess=newList[0];
        sizeOfPage=newList[1];
        numberOfEntries=newList[2];

        listOfLogical=[];
        listPageRequests=0;
        queueOfLogical=[];
        queuePageRequests=0;

#LRU
        for element in range(numberOfEntries):

            currPageRequest=getPage(int(input()),sizeOfPage);

            #FIFO
            if(currPageRequest in queueOfLogical):
                pass;
            elif(len(queueOfLogical)>=numberOfPagesPerProcess):
                queueOfLogical.pop();
                queueOfLogical.insert(0,currPageRequest);
                queuePageRequests+=1;
            else:
                queueOfLogical.insert(0,currPageRequest);

            #Case of in list but not at start:
            if(currPageRequest in listOfLogical):
                listOfLogical.remove(currPageRequest);
                listOfLogical.insert(0,currPageRequest);
        #Case of in list and in first place:
            elif(len(listOfLogical)>=numberOfPagesPerProcess):
                listOfLogical.pop();
                listOfLogical.insert(0,currPageRequest);
                listPageRequests+=1;

            else:
                listOfLogical.insert(0,currPageRequest);


        if(listPageRequests<queuePageRequests):
          print('yes {} {}'.format(queuePageRequests,listPageRequests));
        else:
          print('no {} {}'.format(queuePageRequests,listPageRequests));

main()
