def cacti_number(arr):
    y = len(arr)
    x = len(arr[0])
    count = 0
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 0:
                placible = True
                if i > 0 and arr[i - 1][j] == 1:
                    placible = False
                if i < y - 1 and arr[i + 1][j] == 1:
                    placible = False
                if j > 0 and arr[i][j - 1] == 1:
                    placible = False
                if j < x - 1 and arr[i][j + 1] == 1:
                    placible = False
                
                if placible:
                   arr[i][j] = 1
                   count += 1
    return count
