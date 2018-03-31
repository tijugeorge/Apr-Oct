# Python code to implement iterative Binary 
# Search.
 
# It returns location of x in given array arr 
# if present, else returns -1
#iterative

def binarySearch(arr, l , r, elem):
  while l <= r:
    mid = l + (r-l)//2
    
    if arr[mid] == elem:
      return mid
      
    elif arr[mid] < elem:
      l = mid + 1
      
    else:
      r = mid - 1
  return -1
  
  
arr = [ 2, 3, 4, 10, 40 ]
elem = 10

result = binarySearch(arr, 0, len(arr)-1, elem)
 
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
