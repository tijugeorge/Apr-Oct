#Linear Search
#Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

def linSearch(arr, elem):
  for i in range(len(arr)):
    if arr[i]== elem:
      return i
    else:
      return "Not found"
      

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

print(linSearch(arr, 11))
    
