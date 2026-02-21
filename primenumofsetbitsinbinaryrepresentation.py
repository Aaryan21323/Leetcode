# understandable solution find prime and stuff did it my self except ehe function to find prime
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeNum=0
        for i in range(left,right+1):
            binary=format(i,'b')
            count=0
            for j in binary:
                if j=="1":
                    count+=1

            if self.is_prime(count):
                primeNum+=1

        return primeNum    
                

    def is_prime(self,n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))