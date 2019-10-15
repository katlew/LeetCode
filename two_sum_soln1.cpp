/*
Two Sum
Approach 1: Brute Force
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1].
*/

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            int i,j;
            vector<int> solution;

            for(i=0;i<=nums.size();i++)
            {
                for(j=i+1;j<=nums.size()-1;j++)
                {
                    if(nums[i]+nums[j] == target)
                    {
                        solution.push_back(i);
                        solution.push_back(j);
                        return solution;
                    }
                }
            }
            return solution;
        }
};

/*
Complexity Analysis

Time complexity : O(n^2) For each element, we try to find its complement 
by looping through the rest of the array which takes O(n)O(n) time.
Therefore, the time complexity is O(n^2)

Space complexity: O(1)
*/