"""
Two Sum
Approach 1: Brute Force
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

"""
Complexity Analysis

Time complexity : O(n^2) For each element, we try to find its complement 
by looping through the rest of array which takes O(n)O(n) time. 
Therefore, the time complexity is O(n^2)

Space complexity : O(1) 
"""