class Solution:
    # @param s, a string
    # @return an integer
    # ord(char) - ord('A') = corresponding A:1, B:2
    def titleToNumber(self, s):
        result = 0
        for char in s:
            print "%d * 26 + %d + 1" % (result, ord(char) - ord('A') )
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result
            
