class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i:int = 0
        for char in t:
            if i < len(s):
                if char == s[i]:
                    i +=1   
            else:
                break
        if i < len(s):
            return False
        else:
            return True
#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
S = Solution()
print(S.isSubsequence("abc", "ahbgdc"))
