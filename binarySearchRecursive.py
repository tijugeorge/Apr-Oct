def binarySearch(arr, l, r, x):
  """Interative"""
  while r >= l:
    mid = l + (r-l)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      r = mid - 1
    else:
      l = mid + 1
  return -1


#test
arr = [2,3,5,10,40]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
  print("Element is present at index %d"%result)
else:
  print("Element is not present in array")
