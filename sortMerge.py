arr1 = [2,5,8,9]
arr2 = [1,3,4,7]


def merging(arr1, arr2):
  length = len(arr1)+len(arr2)
  newArr = []
  i, j = 0, 0
  for k in range(length):
    try:
      while i < len(arr1) or j < len(arr2):
        #print(arr1, arr2, newArr)
        if arr1[i] <= arr2[j]:
          newArr.append(arr1[i])
          i += 1
        elif arr1[i] > arr2[j]:
          newArr.append(arr2[j])
          j += 1
    except:
      pass
  if i == len(arr1):
    while j < len(arr2):
      newArr.append(arr2[j])
      j+=1
  if j == len(arr2):
    while i < len(arr1):
      newArr.append(arr1[i])
      i+=1
  return newArr

def insertionSort(arr):
  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
      arr[i+1] = arr[i]
      i = i - 1
    arr[i+1] = key
  return arr



#print(merging(arr1, arr2))


def main(arr1, arr2):
  arr1 = insertionSort(arr1)
  arr2 = insertionSort(arr2)
  return merging(arr1, arr2)


arr1 = [3,6,1,5,3,5]
arr2 = [5,9,0,1,6,3,1,8,3,6]

print(main(arr1, arr2))  
