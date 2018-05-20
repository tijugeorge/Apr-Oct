class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < len(nums):
            nums[:] = nums[-k:]+nums[:-k]
        else:
            for i in range(k):
                nums[:] = nums[-1:]+nums[:-1]
        
