# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# neetcode solution optimal 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode() # for edge case so that the list is not empty
        tail=dummy

        while list1 and list2: # while l1 and l2 are nit empty
            if list1.val < list2.val: # if the value of l2 is less than l2
                tail.next=list1 # set next of tail to l1
                list1=list1.next # set the pointer at l1 to l1 next
            else: # for l1.val>=l2.val
                tail.next=list2 # set the next of tail to l2
                list2=list2.next  # set the pointer at l2 to l2 next
            tail=tail.next # update the tail

        if list1: # l1 is not null after ending
            tail.next=list1 #set the next of the tail to the remaining list cause the list is sorted
        elif list2: # same for l2
            tail.next=list2
        
        return dummy.next