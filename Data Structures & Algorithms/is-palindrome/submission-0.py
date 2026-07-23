class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist=[]
        result=True
        for char in s:
            if char.isalnum():
                charlist.append(char.lower())
        
        i=0 
        j=len(charlist)-1
        for i in range(len(charlist)//2):
            if charlist[i]!=charlist[j]:
                result=False 
                break 
            j-=1
        return result