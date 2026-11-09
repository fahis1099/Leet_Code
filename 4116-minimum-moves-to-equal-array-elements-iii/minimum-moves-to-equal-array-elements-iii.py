class Solution:
    def minMoves(self, nums: List[int]) -> int:
        curr_max, min_moves = 0,0

        for i, num in enumerate(nums):
            if num > curr_max:
                min_moves += (num - curr_max) * i
                curr_max = num
            else:
                min_moves += (curr_max - num)

        return min_moves

        