class Solution(object):
	def getRow(self, rowIndex):
		res = [1 for i in xrange(rowIndex+1)]
		for row in xrange(rowIndex+1):
			for col in xrange(1, row):
				col = row - col
				res [col] += res[col-1]
		return res

"""
rowIndex : 1 	res :[1]

rowIndex : 2	res : [1,1]

rowIndex : 3	res : [1,1,1]
	
"""