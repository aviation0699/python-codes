class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d=set()
        v=[]
        for i in nums:
            if i in d:
                v.append(i)
            else:
                d.add(i)
        return v        
        
