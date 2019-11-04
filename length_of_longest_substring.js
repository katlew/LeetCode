/*
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
*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    d = {};

    for(let end = 0, i = 0; end < s.length; ++end) 
    {
        let currChar = s.charAt(end);
        if (currChar in d)
        {
            i = Math.max(d[currChar], i);
        }
        let difference = end-i;
        maxLength = Math.max(maxLength, difference + 1);
        d[currChar] = end + 1;
    }
    
    return maxLength;
};

/*
Complexity Analysis

Time complexity : O(n). Index end will iterate n times.

Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.

Space complexity (Table): O(m). m is the size of the charset.
*/