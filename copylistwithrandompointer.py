"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None} # we do None : None for a edege case which is if the node is null

        cur=head # intialize the current to the head of the list
        while cur: # while cur is not null
            copy=Node(cur.val) # making a copy of the value if the list
            oldToCopy[cur]=copy # making a hash map and mapping the curr to copy which stores the values
            cur=cur.next # to iterate increase the current

        cur=head # initailze the current to the head again 
        while cur: # while cur is not null
            copy=oldToCopy[cur] # copying the values of the hash map 
            copy.next=oldToCopy[cur.next] # copying the values of the next pointer stored in hashmp
            copy.random=oldToCopy[cur.random] # copying the values of the radom pointer stored in hashmap
            cur=cur.next
        return oldToCopy[head] # as we only need to return the head of the list