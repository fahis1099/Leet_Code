class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = len(needle) - 1

        for i in range((len(haystack) - len(needle)) + 1):
            curr_str = haystack[i:j+1]

            if curr_str == needle:
                return i
            else:
                j += 1
        
        return-1