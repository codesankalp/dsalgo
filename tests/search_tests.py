from dsalgo.Search import Search
array = [2, 4, 6, 8, 10]

# Should output 4
result = Search(array, 'linear', 10)
print(result)

# Should output -1
result = Search(array, 'linear', 12)
print(result)

# Should output 4
result = Search(array, 'binary', 10)
print(result)

# Should output -1
result = Search(array, 'binary', 12)
print(result)