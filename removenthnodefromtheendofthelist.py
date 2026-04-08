# neetcode solution using pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head) # This a dummy node that allows us to place the left pointer at the n position from the end. It points head and starts at 0
        left=dummy # starting left from the dummy
        right=head # start the head from head and it moves n spaces 

        while n>0 and right: # this make it so that the r is at n position before we start
            right=right.next
            n-=1

        while right: # this is fir traversing to the necessary node to delete
            left=left.next
            right=right.next
        
        # delete 
        left.next=left.next.next # removing the nth node

        return dummy.next # as the next of dummy is the actual head