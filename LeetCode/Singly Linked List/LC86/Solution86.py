# https://leetcode.com/problems/partition-list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        header1, header2 = ListNode(0), ListNode(0)
        tail1, tail2 = header1, header2

        headclone = head
        while headclone:
            if headclone.val < x:
                tail1.next = headclone
                tail1 = tail1.next

            else:
                tail2.next = headclone
                tail2 = tail2.next
            headclone = headclone.next
        
        tail1.next = header2.next
        tail2.next = None
        self.head = header1.next
        return header1.next
