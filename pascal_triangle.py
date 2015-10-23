class Solution(object):
  def generate(self, numRows):
    if numRows is 0:   return []

    result = [[1]]
    while len(result) < numRows:
      row = [1]
      previousRow = result[-1]

      for i in xrange( len(previousRow) - 1 ):
        row.append(result[-1][i] + result[-1][i+1])
      
      row.append(1)
      result.append(row)
    return result
"""
Time Complexity O(n^2)

        1
      1   1         
    1   2   1
  1   3   3   1
1     4   6   4   1
 
- 4 rows = 4 items in that row
- every row starts and ends with 1

4th row
- for i in (3-1) = 2:
  result[2][0] + result[2][1] = 1 + 2 = 3
  result[2][1] + result[2][2] = 2 + 1 = 3

5th row
- for i in (4-1) = 3:
  0 : result[3][0] + result[3][1] = 1 + 3 = 4
  1 : result[3][1] + result[3][2] = 3 + 3 = 6
  2 : result[3][2] + result[3][3] = 3 + 1 = 4

"""