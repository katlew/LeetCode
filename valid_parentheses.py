class Solution(object):
	def isValid(self, s):
		stack = []
		matchingTable = {"(":")", "[":"]", "{":"}"}

		for char in s:
			if self.isOpen(char):
				stack.append(char)
			elif self.isClosed(char):
				if len(stack) == 0 or char != matchingTable[stack.pop()]:
					return False
				else:
					pass
		return len(stack) == 0

	def isOpen(self, c):
		open_brackets = {"(", "{", "["}
		return c in open_brackets
	def isClosed(self, c):
		closed_brackets = {")", "}", "]"}
		return c in closed_brackets

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.


- maintain 1
- ( )   []   {}
- if it's an open, push
- if it's close
 - make sure closed character is ==> matchinTable["("] = ")
- if there's anything left in any of the stack, return false

"""