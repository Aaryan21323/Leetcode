# tried to do it myself but got stuck in no 13 should seee it again 

# workind soln

class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        position = 0
        max_distance = 0
        
        while n > 0:
            if n & 1:  # if last bit is 1
                if last != -1:
                    max_distance = max(max_distance, position - last)
                last = position
            n >>= 1
            position += 1
        
        return max_distance
    

# conversion soln

class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n, 'b')
        prev = -1
        max_distance = 0
        
        for i in range(len(binary)):
            if binary[i] == '1':
                if prev != -1:
                    max_distance = max(max_distance, i - prev)
                prev = i
        
        return max_distance