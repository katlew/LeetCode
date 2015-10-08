class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        d = set()
        for num in nums:
            if num in d:
                return True
            else:
                d.add(num)
        return False