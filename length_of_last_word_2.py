class Solution(object):
    def lengthOfLastWord(self, s):
        preLength = 0       # length of previous word 
        length = 0

        for letter in s:
            if letter == " ":
                if length != 0:
                    preLength = length
                    length = 0
                else:
                    pass
            else:
                length += 1
        if length == 0:
            return preLength
        else:
            return length