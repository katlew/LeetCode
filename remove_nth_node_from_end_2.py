class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None: return None

        former, latter = head, head

        for _ in xrange(n-1):
            latter = latter.next

        # if node is last item, remove front
        if latter.next is None:
            head = head.next
        else:
            latter = latter.next

            while latter.next is not None:
                former = former.next
                latter = latter.next
            # remove the nth node from end
            former.next = former.next.next

        return head
"""

1 2 3 4 5
former, latter = 1,1
latter = 1

latter = 2
former = 2 latter = 3
former = 3 latter = 4

3->5
return head
"""