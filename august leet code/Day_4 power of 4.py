class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        #n=num
        if num < 1:
            return False
        while num%4 == 0:
            num /= 4
        return True if num==1 else False
        
