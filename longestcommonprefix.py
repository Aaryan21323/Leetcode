class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take first string as reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this position in all other strings
            for j in range(1, len(strs)):
                # If we reach end of a string or find mismatch
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]  # First string is the common prefix