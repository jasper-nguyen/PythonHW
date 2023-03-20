
def palindrome(list):
    theList = list
    mid = int(len(list) / 2)
    firHalf = theList[:mid]
    halfTwo = list[mid:]
    listCheck = halfTwo[::-1]
    if len(list) == 1:
        return True
    elif firHalf == listCheck:
        return True
    else:
        return False

