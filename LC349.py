class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    res.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    res.append(i)
        return [i for i in set(res)]
