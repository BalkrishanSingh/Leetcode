class Solution:
    def isValid(self, s: str) -> bool:
        stack:list[str] = []
        match:dict[str,str] = {
            ')': '(', '}': '{', ']':'['
        }
        i:int = 0
        while i < (len(s)):
            if s[i] in match.values():
                stack.append(s[i])
            else:
                if stack and stack[-1] == match[s[i]]:
                    stack.pop()
                else:
                    return False
            i +=1 

        return not stack

#https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150