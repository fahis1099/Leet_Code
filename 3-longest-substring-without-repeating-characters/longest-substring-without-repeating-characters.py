class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        j = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= j:
                j = dic[s[i]] + 1

            dic[s[i]] = i
            max_len = max(max_len, i - j + 1)
        
        return max_len