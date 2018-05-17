def findDisappearedNumbers(nums):
  res  = []
  for num in nums:
    nums[abs(num) - 1] = abs(nums[abs(num) - 1])* -1
  
  print(nums)  
  for i in range(len(nums)):
    if nums[i] > 0:
      res.append(i+1)
  return res
  
  
  
nums = [4,3,2,7,8,2,3,1]


print(findDisappearedNumbers(nums))
