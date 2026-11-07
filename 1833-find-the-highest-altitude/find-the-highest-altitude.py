class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = 0
        mx = 0

        for g in gain:
            alt += g
            mx = max(mx,alt)
        
        return mx