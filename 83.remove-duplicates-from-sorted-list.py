#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
from typing import Optional,ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur=head
        while cur:
            if cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head





        
# @lc code=end
