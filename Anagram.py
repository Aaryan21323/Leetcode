#neetcode solution

class Solution():
    def anagram(self,s:str,l:str)->bool:
        if sorted(s)==sorted(l):
            return True
        else:
            return False
    

