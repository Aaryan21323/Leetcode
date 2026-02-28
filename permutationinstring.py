# need to study this ( really harrd problem )
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        # Build frequency for s1 and first window of s2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character
            count2[ord(s2[i]) - ord('a')] += 1
            
            # Remove old character
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if count1 == count2:
                return True
        
        return False
    

# neetcode solution super optimized version ??

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        # Build frequency arrays
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # Count initial matches
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            
            # If all 26 characters match
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            count2[index] += 1
            
            # Check if this update creates or breaks a match
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1
            
            # Remove left character
            left_index = ord(s2[l]) - ord('a')
            count2[left_index] -= 1
            
            if count1[left_index] == count2[left_index]:
                matches += 1
            elif count1[left_index] - 1 == count2[left_index]:
                matches -= 1
            
            l += 1
        
        return matches == 26

