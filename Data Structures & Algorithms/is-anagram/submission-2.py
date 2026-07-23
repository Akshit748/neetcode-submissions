class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}
        result=True
        if len(s)!=len(t):
            return False 
        for char in s:
            if char in hash:
                hash[char] +=1
            else:
                hash[char]=1
        
        for char in t:
            if char in hash:
                hash[char] -=1
        for i in hash:
            if hash[i]!=0:
                result = False
                break
        return result 
        