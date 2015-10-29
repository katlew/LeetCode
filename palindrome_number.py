class Solution(object):
    def isPalindrome(self, x):
        if x < 0:               return False
        if x >= 0 and x < 10:   return True
    
        array = self.intToArray(x)
        mid = len(array)//2             # floor division
        for i in xrange(mid):
            if array[i] != array[-i-1]:
                return False
        return True

    def intToArray(self, x):
        array = []
        while x / 10 != 0:
            array.append(x%10)
            x /= 10
        array.append(x)
        return array[::-1]
        # returns the result in reverse order

"""
* put in an array
* split in half
* compare first and last integers

5 // 2 = 2
0 1 2 3 4 
_ _  _ _ 

4//2 = 2
if it's even, 0 - mid 
0 1 2 3 
_ _ _ _ 

"""