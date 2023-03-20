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



list1 = [1,3,5,7]
list2 = [2,4,6]
print(merge(list1, list2))
list3 = [1,2,3,5]
list4 = [1,2,4,5,6]
print(merge(list3, list4))
list5 = [1,5,9]
list6 = []
print(merge(list5, list6))