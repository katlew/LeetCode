class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()   # remove beginning / end space
        length = 0
        for letter in s:
            if letter == " ":   
                length = 0
            else:               
                length += 1
        return length
