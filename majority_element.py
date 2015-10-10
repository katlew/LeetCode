class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [i, count]
        # take max amount of count
        d = dict()
        for n in nums:
            if n not in d:
                d[n]=0
            else:
                d[n] += 1
        return max(d, key=d.get) # gets key w/ max value
            
        