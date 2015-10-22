class Solution(object):
	def plusOne(self, digits):
		digit = digits[::-1]	# reverse array
		n = len(digits)
		temp = 0
		carry = 1
		i = 0
		result = []
		while i < n or carry > 0:
			temp = 0
			if i < n:
				temp += digits[i]
			if carry > 0:
				temp += carry
			digit = temp % 10
			carry = temp / 10
			result.append(digit)
			i += 1
		return result [::-1]

"""
The [::-1] slice reverses the list 
in the for loop (but won't actually modify your list


[7,8,9]
[9,8,7]
i = 0, carry = 0, temp = 0, temp = 9, temp = 10, digit = 0, carry = 1
i = 1, carry = 1, temp = 0, temp = 8, temp = 9, digit = 9, carry = 0
i = 2, carry = 0, temp = 0, temp = 7, temp = 7, digit = 7, carry = 0
[7,9,0]

"""