class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, c in enumerate(nums):
            if c != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
