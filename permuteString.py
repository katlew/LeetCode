# Permutations of String
# Write a program to print all permutations of a given string, duplicates allowed

def permute(list a, int start, int end):
	if start == end:
		print "%s" % a
	else:
		for i in xrange(start, end+1):
			a[start], a[i] = a[i], a[start]
			permute(a, start+1, end)
			a[start], a[i] = a[i], a[start]


## Driver function
string = "ABC"
a = list(string)
n = len(string)
permute(a, 0, n-1)
# Geeks for Geeks - http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

