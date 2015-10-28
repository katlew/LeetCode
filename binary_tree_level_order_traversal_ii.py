class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []

        result = []
        nextLayer = [root]
        # store nodes
        while len(nextLayer) != 0:
            result.append(nextLayer)

            # gather nodes in next deeper layer
            nextLayer = []
            for parent in result[-1]:
                if parent.left is not None:
                    nextLayer.append(parent.left)
                if parent.right is not None:
                    nextLayer.append(parent.right)

        # convert the nodes into their values
        result = [[node.val for node in layer] for layer in result]

        return result[::-1]
        # returns backwards