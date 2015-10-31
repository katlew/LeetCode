class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:    
            return None
        elif n == 0:
            return head
        else:
            # pp -> p
            q = p = pp = head
            while q is not None:
                if n <= 0:
                    pp = p
                    p = p.next
                q = q.next
                n -= 1
            # remove head node
            if pp is p:
                head = pp.next
            else:
                pp.next = p.next
                # free p
            return head

"""
1 2 3 4 5 
q, p, pp, = 1
n = 2, q = 2
n = 1, q = 3
n = 0, pp = 1, p = 2, q = 4
n = -1, pp = 2, p = 3, q = 5
n = -2, pp = 3, p = 4, q = None

3->5

"""