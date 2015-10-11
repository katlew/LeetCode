class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0 for i in range(n + 1)] # [0, 0, 0, 0, 0, 0, 0]
        return self.climb(n, t)

    def climb(self, n, t):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif t[n] != 0:
            return t[n]
        else:
            t[n] = self.climb(n - 1, t) + self.climb(n - 2, t)
            print "self.climb(%d - 1)" % (n-1)
            print "%d + %d" % (self.climb(n-1,t), self.climb(n-2,t))
            print t[n]
            return t[n]
