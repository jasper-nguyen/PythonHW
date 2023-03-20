def merge(list1, list2):
    firstList = list1
    secondList = list2
    sortedList = []

    if len(firstList) == 0:
        return secondList
    if len(secondList) == 0:
        return firstList

    while(firstList and secondList):
        if(firstList[0] < secondList[0]):
            sortedList.append(firstList.pop(0))
        else:
            sortedList.append(secondList.pop(0))
    while(firstList):
        sortedList.append(firstList.pop(0))
    while(secondList):
         sortedList.append(secondList.pop(0))
    return sortedList



