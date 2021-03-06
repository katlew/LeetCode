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
            map<int, int> m = {};
            vector<int> solution;

            for (int i = 0; i < nums.size(); ++i)
            {
                m.insert(pair<int, int>(nums[i], i));
            }

            for(int i = 0; i < nums.size(); ++i)
            {
                int complement = target - nums[i];
                if (m.count(complement)>0 && m.at(complement) != i)
                {
                    solution.push_back(i); 
                    solution.push_back(m.at(complement));
                    return solution;
                }
            }
            return solution;
        }
};

/*
Complexity Analysis:

Time complexity: O(n).
We traverse the list containing nn elements exactly twice.
Since the hash table reduces the lookup time to O(1),
the time complexity is O(n).

Space Complexity: O(n)
The extra space required depends on the number of items stored in the hash table,
which stores exactly n elements.
*/