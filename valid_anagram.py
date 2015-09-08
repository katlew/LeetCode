# An anagram is a type of word play, the result of rearranging the letters of a word or phrase
# to produce a new word or phrase, using all the original letters exactly once

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict = {};
        sArray = list(s)
        tArray = list(t)
        # initialize dictionary with all of the keys / letters
        for i in sArray:
            dict[i] = dict[i]+1 if dict.has_key(i) else 1
        for i in tArray:
            dict[i] = dict[i]-1 if dict.has_key(i) else -1
            if dict[i] < 0:
                return False
        return True
