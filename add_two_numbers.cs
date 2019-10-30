/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

// 2 4 3
// 5 6 4
// 7 0 8
*/

/**
* Definition for singly-linked list.
* public class ListNode {
*     public int val;
*     public ListNode next;
*     public ListNode(int x) { val = x; }
* }
*/

public class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode headNode = new ListNode(0);
        ListNode currentNode = headNode;
        ListNode x = l1;
        ListNode y = l2;
        int carry = 0;
        
        while(x != null || y != null)
        {
            int a = (x != null) ? x.val : 0;
            int b = (y != null) ? y.val : 0;

            int sum = carry + a + b;
            carry = sum / 10;
            currentNode = currentNode.next = new ListNode(sum % 10);

            if (x != null) { x = x.next; }
            if (y != null) { y = y.next; }
        }

        if (carry == 1)
        {
            currentNode.next = new ListNode(1);
        }

        return headNode.next;
    }
}

/*
Complexity Analysis

Time complexity : O(max(m,n)). 
Assume that m and n represents the length of l1 and l2 respectively, 
the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). 
The length of the new list is at most max(m,n)+1.
*/