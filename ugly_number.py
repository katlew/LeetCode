class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        while(num > 1):
            if num % 5 == 0:
                num /= 5
            elif num % 3 == 0:
                num /= 3
            elif num % 2 == 0:
                num /= 2
            else:
                return False
        return True
