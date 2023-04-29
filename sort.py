def sort_dictionary(theDict): 
   sortedDict = dict(sorted(theDict.items(), key=lambda item: item[1][1]))
   output = [(k, v[0]) for k, v in sortedDict.items()]
   return output
