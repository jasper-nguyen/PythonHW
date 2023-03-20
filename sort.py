def sort_dictionary(dictionary):
    rev = dict(reversed(list(dictionary.items())))
    return rev

dictionary =  {"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}
print(sort_dictionary(dictionary))