class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        last_symbol:str = " "
        for i in s:
            if  i in "VXLCDM" and last_symbol in "IXC":
                if i == "V" and last_symbol == "I":
                    sum +=3
                    last_symbol = " "
                elif i == "X" and last_symbol == "I":
                    sum +=8
                    last_symbol = " "
                elif i == "L" and last_symbol == "X":
                    sum +=30
                    last_symbol = " "
                elif i == "C" and last_symbol == "X":
                    sum +=80
                    last_symbol = " "
                elif i == "D" and last_symbol == "C":
                    sum +=300
                    last_symbol = " "
                elif i == "M" and last_symbol == "C":
                    sum +=800
                    last_symbol = " "
            elif i in "VLDM" and last_symbol == " ":
                if i == "V" :
                    sum +=5
                    last_symbol = " "
                elif i == "L":
                    sum +=50
                    last_symbol = " "
                elif i == "D":
                    sum +=500
                    last_symbol = " "
                else:
                    sum +=1000
                    last_symbol = " "
            elif i in "IXC":
                if i == "I":
                    sum +=1
                    last_symbol = "I"
                elif i == "X":
                    sum +=10
                    last_symbol = "X"
                elif i == "C":
                    sum +=100
                    last_symbol = "C"
           
            
        return sum
a = Solution()
a.romanToInt("DCXXI")
#https://leetcode.com/problems/roman-to-integer/solutions/5848685/video-looping-two-characters-at-a-time-b-squ4/?envType=study-plan-v2&envId=top-interview-150