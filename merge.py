def merge (list1, list2):
    output = []
    while (list1 and list2):
        if (list1[0] < list2[0]):
            output.append(list1.pop(0))
        else:
            output.append(list2.pop(0))
    while (list1):
        output.append(list1.pop(0))
    while (list2):
        output.append(list2.pop(0))
    return output
