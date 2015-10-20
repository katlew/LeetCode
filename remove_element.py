class Solution(object):
    def removeElement(self, nums, val):
    	front, back = 0, 0
    	while front < len(nums):
    		if nums[front] != val:
    			nums[back] = nums[front]
    			back += 1
    		front += 1
    	return back