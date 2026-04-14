# neetcode solution Floyd's Tortoise and Hare Solution
# most optimal T(n):O(n) and S(n):O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head # initialize the slow and fast pointer 

        while fast and fast.next:# while fast and fast.next are not null
            slow=slow.next # slow pointer moves 1 
            fast=fast.next.next # fast pointer moves 2
            if slow==fast: # if fast and slow are equal return True
                return True
        return False # if loop exits return False