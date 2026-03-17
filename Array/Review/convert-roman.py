class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman_values:dict = {
            "I"     :      1, 
            "V"     :      5,
            "X"     :      10,
            "L"     :      50,
            "C"     :      100,
            "D"     :      500,
            "M"     :      1000
        }
        for i,literal in enumerate(s[:len(s)-1]):
            if roman_values[literal] < roman_values[s[i+1]]:
                sum -= roman_values[literal]
            else:
                sum += roman_values[literal]
                
        return sum + roman_values[s[-1]]
#https://leetcode.com/problems/roman-to-integer/solutions/5848685/video-looping-two-characters-at-a-time-b-squ4/?envType=study-plan-v2&envId=top-interview-150