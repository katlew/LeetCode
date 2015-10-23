class Solution(object):
    def rob(self, nums):
        if len(nums) is 0:		return 0
        if len(nums) <= 2:	return max(nums)

    	else:
    		max_money = [0] * len(nums)
    		max_money[0] = nums[0]
    		max_money[1] = max(nums[0], nums[1])

    		for house in xrange(2, len(nums)):
    			max_money[house] = max(max_money[house-1], max_money[house-2]+nums[house])
    		return max_money[-1]



"""
[0] 1 [2] 3 4 5 
 0	2  3  40

max_money - positions

[0, max(0,1), max[1, or 0+2]]

[0, 0, 2]
[0, 1, 1]


for 2:
	max_money[2] = max( max_money[1], max_money[0] + nums[2] )
	3:
	max_money[3] = max( max_money[2], max_money[1] + nums[3] )

Loop 2 
max_money = [0, 2, (2,0+3),]
max_money = [0, 2,    3]

Loop 3
max_money = [0, 2, 3, (3, 2 + 40)]
max_money = [0, 2, 3, 42]

"""