# my own solution (there may be an easy way to do this but i did it myself so yahh)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        revstr=s[::-1] # first ew reverse the string
        flag=0  # flag to detect the spaces after words
        count=0 # to count the nuber of words
        for i in range(len(revstr)):  # we loop through the reversed string
         if revstr[i]==" " and flag==0:  # this detects the white spaces and check that no words are there and pass
            pass
         elif revstr[i]==" " and flag==1: # this detects the whitespaces after the letter and stops the loop when the flag is 1
            break
         elif revstr[i].isalnum(): # this detects the last word which is the first word in reversed string and sets the flag to 1 and also count the word count
            flag=1
            count+=1
            pass
        return count # return the count of the word 

# pythonic way seems much easier but we used built in function     
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1]) # .strip removes the leading and trailing spaces and .spilt automatically splits the spaces and returns list and [-1] gets the last word
        
# solution without reversing the string better than my solution cause of no extra string, no flag, very clan logic and O(1) space
class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length
    

s = "   fly me   to   the moon  "
sol=Solution()
print(sol.lengthOfLastWord(s))