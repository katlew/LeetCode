class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
    	if nums is None or k is None or k is 0: return False
        dictionary = dict()
        containsDuplicate = False
        kDifference = False
        for i in xrange(len(nums)):
        	if dictionary.has_key(nums[i]):
        		containsDuplicate = True
        		dictionary[nums[i]].append(i)
        	else:
        		dictionary[nums[i]] = [i]
        print dictionary
        if containsDuplicate is False:
			return False
		for value in dictionary.itervalues():
			for i in len(1, value):
				if abs(abs(value[i-1]) - abs(value[i])) <= k:
					return True
		return False


"""
Given an array of integers and an integer k
find out if there are 2 distinct indices 
i and j in the array such that nums[i] = nums[j] 
and the difference between i and j is at most k.

							value [indices]
dictionary = {key, value} : {1, [0,3,5]}
"""