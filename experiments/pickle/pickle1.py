import pickle

a = {'hello': 'world'}

with open('pickle1', 'wb') as handle:
  pickle.dump(a, handle)

with open('pickle1', 'rb') as handle:
  b = pickle.load(handle)

print (a == b)
