class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I II III IV V VI VII VIII VIIII X
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000
        #  a letter placed after another of greater value adds (thus XVI or xvi is 16), whereas a letter placed before another of greater value subtracts (thus XC or xc is 90)
        
        # greater, less = greater + less
        # less, greater = -1*less + 5
        # less, greater, less
        # XIV = greater, less, greater = 10 + (-1) + 5
        d = dict({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000})
        sum = 0
        i = 0
        for i in range(len(s)-1):
            if d[s[i+1]] > d[s[i]]:
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
            print d[s[i]]
            ++i
        sum += d[s[len(s)-1]]
        return sum
            
        