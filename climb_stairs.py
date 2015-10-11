class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ''' The number of distinct ways to take n steps is
            the Fibonacci number.
            http://en.wikipedia.org/wiki/Fibonacci_number
            Negative numbers mean that you count from the right instead of the left. 
            So, list[-1] refers to the last element, list[-2] is the second-last, and so on.
        '''
        steps = [1, 1]
        while len(steps) < n + 1:
            steps.append(steps[-1] + steps[-2])
            
        return steps[n]