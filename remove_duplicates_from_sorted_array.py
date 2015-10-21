class Solution(object):
    def removeDuplicates(self, nums):
    	front, back = 1, 1

    	if len(nums) == 0:
    		return 0
    	
    	while front < len(nums):
    		if nums[front] != nums[front-1]:
    			nums[back] = nums[front]
    			back += 1

    		front += 1
    	return back