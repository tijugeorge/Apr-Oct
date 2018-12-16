# Linear Search
#Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

def linearSearch(s, x):
  for index in range(len(s)):
    if s[index] == x:
      return index
  return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

print(linearSearch(arr, 110))


