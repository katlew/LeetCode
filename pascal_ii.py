class Solution(object):
	def getRow(self, rowIndex):
		res = [1 for i in xrange(rowIndex+1)]
		for row in xrange(rowIndex+1):
			for col in xrange(1, row):
				col = row - col
				res [col] += res[col-1]
		return res

"""
rowIndex : 1 	res :[1,1]

rowIndex : 2	res : [1,2,1]

rowIndex : 3	res : [1,1,1,1]
	row : 1 of 3
	row : 2 of 3
		col : 1 of 2
			col = 2-1 = 1
			res[1] = res[1] + res[0] = 1+1 = 2
	row : 3 of 3
		col : 1 of 3
			col : 3-1 = 1
			res[2] = res[2] + res[1] = 1 + 2 = 3
		col : 2 of 3
			col : 3-2 = 1
			res[1] = res[1] + res[0] = 2 + 1 = 3
[1,3,3,1]
"""