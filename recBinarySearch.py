#Binary Search
#Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]
#recursive

def binSearch(arr, l, r, elem):
  if r >= l:
    mid = l + (r - l)//2
    
    if arr[mid] == elem:
      return mid
      
    elif arr[mid] > elem:
      return binSearch(arr, l, mid-1, elem)
      
    else:
      return binSearch(arr, mid+1, r, elem)
      
  else:
    return -1
    
    
arr = [ 2, 3, 4, 10, 40 ]
elem = 10

result = binSearch(arr, 0, len(arr)-1, elem)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
