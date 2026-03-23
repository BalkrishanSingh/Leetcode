class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        max_prefix = strs[0]
        for i in strs[1:]:
            if max_prefix == "":
                break
            while max_prefix != "":
                if i.startswith(max_prefix):
                    break
                else:
                    max_prefix = max_prefix[:-1]
        return max_prefix
           

             
