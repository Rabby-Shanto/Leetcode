#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
from types import Optional,ListNode
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head

        while (slow_pointer != None and fast_pointer != None and fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return 1
        return 0


        
# @lc code=end

