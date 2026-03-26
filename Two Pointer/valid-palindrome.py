class Solution:
    def isPalindrome(self, s: str) -> bool:

        i:int = 0
        j:int = len(s) -1
        s = s.lower()

        
        while i < j:
            while not s[i].isalnum() and i < j:
                i+=1
            while not s[j].isalnum() and i < j:
                j-=1
            if s[i] != s[j]:
                return False
            i +=1
            j -=1
        return True
#https://leetcode.com/problems/valid-palindrome/submissions/1959879418/?envType=study-plan-v2&envId=top-interview-150
             
        

        