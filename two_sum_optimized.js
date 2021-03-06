/**
 * Two Sum
 * Approach 1: Brute Force
 * Given an array of integers, return indices of the two numbers such that 
 * they add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, 
 * and you may not use the same element twice.
 *
 * Example:
 *
 * Given nums = [2, 7, 11, 15], target = 9,
 *
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * It turns out we can do it one-pass.
 * While we iterate and insert elements into the table,
 * we also look back to check if current element's complement already exists
 * in the table.
 * If it exists, we have found a solution and return immediately
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target)
{
    var res = [];
    var d = {};
    for (var i = 0; i < nums.length; ++i)
    {
        var complement = target - nums[i];
        if (complement in d && d[complement] != i)
        {
            res.push(i);
            res.push(d[complement]);
            return res;
        }
        d[nums[i]] = i;
    }
};

 /*
Complexity Analysis

Time complexity : O(n) 
We traverse the list containing n elements only once. 
Each look up in the table costs only O(1) time.

Space complexity : O(n) 
The extra space required depends on the number of items stored in the hash table, 
which stores at most n elements. 
*/