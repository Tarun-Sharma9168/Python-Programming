def filter_list(lst):
      return [x for x in lst if type(x) is int]
print(filter_list([1,2,0,15]))
