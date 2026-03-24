class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ammo:dict[str,int] = {}
        for i in magazine:
            if i in ammo:
                ammo[i] += 1
            else:
                ammo[i] = 1
        for i in ransomNote:
            if i not in ammo:
                return False
            else:
                if ammo[i] > 0:
                    ammo[i] -= 1
                else:
                    return False
        return True
#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
# it could be optimised for time by instead using a comparison instead decrementing