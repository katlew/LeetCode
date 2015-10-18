class Solution(object):
	def isHappy(self, n):
		sum_array = set()	# check infinite loop - stores all sums to make sure they don't repeat 
		while n not in sum_array:
			sum_array.add(n)
			print sum_array
			_sum = 0
			num_array = self.splitNumIntoArray(n)
			for num in num_array:
				_sum += pow(num,2)
			print _sum
			if _sum == 1:
				return True
			n = _sum
		return False

	def splitNumIntoArray(self, n):
		num_array = []
		while n != 0:
			num_array.append(n % 10)
			n /= 10
		return num_array

        

"""
123 % 10 = 3
123 / 10 = 12
12 % 10 = 2
12 / 10 = 1
1 % 10 = 1

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.
Example: 19 is a happy number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""