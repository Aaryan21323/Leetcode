# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
 # neetcode solution merge sort way        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            mergedLists=[]

            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.mergeLists(l1,l2))
            lists=mergedLists
        return lists[0]

    def mergeLists(self, list1, list2) :
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