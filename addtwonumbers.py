# neet code solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode() # creating a dummy list for the output
        cur=dummy # intializing the current as dummy
        carry=0
        while l1 or l2 or carry: # conditions 1. while l1 is not null 2. while l2 is not null 3. while th carry is not null as it is needed in the last of the result for eg 7+8=15 where 1 is the carry and needs to be put in the last  (all are edge cases)  
            v1=l1.val if l1 else 0 # value1 = l1.val if l1 in not null else 0
            v2=l2.val if l2 else 0 # value2 = l2.val if l1 in not null else 0

            # new digit
            val=v1+v2+carry

            # for carry eg 15
            carry=val//10 # getting the carry
            val=val%10  # getting the required value
            cur.next=ListNode(val) # adding the value ??

            # updating pointers
            cur=cur.next # updating cur
            l1=l1.next if l1 else None # updating l1 if l1 is not null else we pull null
            l2=l2.next if l2 else None # updating l2 if l2 is not null else we pull null

        return dummy.next