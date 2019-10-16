/*
Two Sum
Approach 2: Two-pass Hash Table
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

A simple implementation uses two iterations.
In the first iteration, we add each element's value and its index to the table.
Then, in the second iteration we check if each element's complement
(target - nums[i])
exists in the table. 
Beware that the complement must not be nums[i] itself!
*/

class Solution {
    public:
        vector<int> twoSum(vector<int> &nums, int target){
            
        }
}