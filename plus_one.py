class Solution(object):
    def plusOne(self, digits):
    	number_array = []
    	one = [1]
    	bool carry_one = False
    	for digit in digits:
    		number = convert_single_digit(digit)
    		number_array.append(number)

    	for i in xrange(len(number_array),0,-1):
    		if i == len(number_array)-1:
    			number_array[i] = number_array[i]+1
    			if number_array[i] > 9:
    				number_array[i] = 0
    				carry_one = True
    		else:
    			if i == 0:
    				if carry_one:
    					if number_array[i] + 1 > 9:
    						number_array[i] = 0
    						number_array = one.append(number_array)
    			elif carry_one:
    				number_array[i] = number_array[i]+1
    				if number_array[i] > 9:
    					 carry_one = True
    				else:
    					carry_one = False
        
        	
        	        
	def convert_single_digit(digit):
		number = []
		if digit > 9:
			while digit > 9:
				number.append(digit % 10)
				digit /= 10
			number.append(digit)
		return number[::-1]
	"""
    To avoid the confusion: reversed() doesn't modify the list. 
    reversed() doesn't make a copy of the list (otherwise it would require 
    O(N) additional memory). If you need to modify the list use alist.reverse(); 
	if you need a copy of the list in reversed order use alist[::-1]

	# traverse through all digits
        # check if each digit is 1 digit 
        # if it's not one digit
        	# "
        	        # create a new array that all has 1 digit each
        	        
        	        # add 1 to the last item
        	        # if number is 9, make it to 0,
        	        # carry over the 1 to the 2nd to last item
        	        # The [::-1] slice reverses the list in the for loop (but won't actually modify your list 
	"""