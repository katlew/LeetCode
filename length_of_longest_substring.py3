"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        d = {}
        i = 0
        for end in range(len(s)):
            currChar = s[end]
            if (currChar in d):
                i = max(i, d[currChar])
            difference = end - i
            maxLength = max(maxLength, difference + 1)
            d[currChar] = end + 1

        return maxLength

"""
Complexity Analysis

Time complexity : O(n). Index end will iterate n times.

Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.

Space complexity (Table): O(m). m is the size of the charset.
"""