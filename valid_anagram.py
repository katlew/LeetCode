# An anagram is a type of word play, the result of rearranging the letters of a word or phrase
# to produce a new word or phrase, using all the original letters exactly once

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) is not len(t):
            return False
        dict = {};
        sArray = list(s)
        tArray = list(t)
        updatedCount = 0;
        solution = True
        # initialize dictionary with all of the keys / letters
        for i in sArray:
            count = dict[i]+1 if dict.has_key(i) else 1
            dict.update({i:count})
        size = len(sArray)
        for i in tArray:
            # print dict.items()
            if dict.has_key(i):
                # decrement the count of the value if tArray has the same char
                updatedCount = dict[i]-1
                # print size
                if updatedCount >= 0:
                    dict.update({i:updatedCount})
                    size = size - 1
                else:
                    return False
        print dict.items()
        print size
        solution = True if size == 0 else False
        # print solution
        return solution
