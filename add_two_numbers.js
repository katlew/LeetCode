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
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2){
    let carryOver = 0;
    const rootNode = new ListNode(null);
    let nodeIterator = rootNode;
    let currentVal;

    while (l1 || l2) {
        if (l1 && l2) {
            currentVal = l1.val + l2.val + carryOver;
        }
        else if (l1){
            currentVal = l1.val + carryOver;
        } 
        else {
            currentVal = l2.val + carryOver;
        }

        carryOver = Math.floor(currentVal / 10);

        const newNode = new ListNode(currentVal % 10);
        nodeIterator.next = newNode;
        nodeIterator = nodeIterator.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }

    if (carryOver) nodeIterator.next = new ListNode(1);

    return rootNode.next;
}

/*
Complexity Analysis

Time complexity : O(max(m,n)). 
Assume that m and n represents the length of l1 and l2 respectively, 
the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). 
The length of the new list is at most max(m,n)+1.
*/