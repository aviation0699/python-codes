class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=''
        for i in s:
            if i.isalnum()==True :
                p+=i.lower()
        #print(p)        
        if p==p[::-1]:
            return True
        else:
            return False
