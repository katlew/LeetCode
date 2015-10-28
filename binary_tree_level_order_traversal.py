class Solution(object):
	def levelOrder(self, root):
		if root is None:
			return []
		result = []
		nextLayer = [root]

		while len(nextLayer) != 0:
			result.append(nextLayer)

			nextLayer = []
			for parent in result[-1]:
				if parent.left is not None:
					nextLayer.append(parent.left)
				if parent.right is not None:
					nextLayer.append(parent.right)
		result = [[node.val for node in layer] for layer in result]

		return result