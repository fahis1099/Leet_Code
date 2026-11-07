class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = [0]

        for g in gain:
            alt.append(alt[-1] + g)
        
        return max(alt)