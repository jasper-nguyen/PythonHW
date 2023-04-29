def palindrome(list):
    pal = True
    count = 0
    while (count < len(list) / 2):
        if (list[count] != list[len(list) - (count + 1)]):
            pal = False
        count = count + 1
    return pal
