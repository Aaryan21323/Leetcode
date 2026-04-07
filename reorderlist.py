# neet code solution not using extra space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the middle using slow(moves 1) and fast(moves 2) pointer 
        slow,fast=head,head.next
        while fast and fast.next: # while the fast and fast.next is not null
            slow=slow.next # moving 1 space
            fast=fast.next.next # moving 2 spaces

        # reverse the second half
        second=slow.next #intialize the second to slow the next
        prev = slow.next=None # slow.next and prev are  null / broken to reverse the second one

        while second: 
            tmp=second.next 
            second.next=prev
            prev=second
            second=tmp 

         # merge the 2 list
        first=head
        second=prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2