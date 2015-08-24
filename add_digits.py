class Solution:
    # @param {integer} num
    # @return {integer}
    # accounting for 9 % 9 = 0, (9-1)%9 + 1 = 8
    def addDigits(self, num):
        if num == 0:
            return 0
        return (1+(num-1) % 9)
