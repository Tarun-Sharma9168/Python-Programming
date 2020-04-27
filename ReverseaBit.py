def name_shuffle(name):
  a, b = name.split()
  a, b = b, a
  return ' '.join((a, b))
print(name_shuffle("Tarun Sharma"))	