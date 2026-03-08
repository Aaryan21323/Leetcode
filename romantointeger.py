class Solution:
    def romanToInt(self, s: str) -> int:
        # Map individual symbols to values
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            # If current value is less than next value, subtract it
            if i < n - 1 and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        
        return result