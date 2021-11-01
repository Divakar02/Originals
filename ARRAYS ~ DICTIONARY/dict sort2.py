test_dict={'a':"Hello",
      "b":"1",
      'c':'Jayaltha',
      'd':[1,2]}
res = ' '.join(sorted(test_dict, key = lambda key: len(test_dict[key])))

print(res)