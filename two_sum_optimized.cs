/*
Two Sum
Optimized
Approach 3: One-pass Hash Table
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

It turns out we can do it in one-pass. 
While we iterate and inserting elements into the table, 
we also look back to check if current element's complement already exists in the table. 
If it exists, we have found a solution and return immediately.
*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
    	
    	IDictionary<int, int> dict = new Dictionary<int, int>();

    	for(int i = 0; i < nums.Length; ++i)
    	{
    		int complement = target-nums[i];
    		if (dict.ContainsKey(complement) && dict[complement] != i)
    		{
    			return new int[] {dict[complement], i};
    		}

    		dict[nums[i]] = i;
    	}
    	throw new Exception("No two sum solution");
	}
}

/*
Complexity Analysis

Time complexity : O(n) 
We traverse the list containing nn elements only once. 
Each look up in the table costs only O(1) time.

Space complexity : O(n) 
The extra space required depends on the number of items stored in the hash table, 
which stores at most n elements. 
*/