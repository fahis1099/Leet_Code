class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            bal = target - nums[i]
            
            if bal in seen:
                return ([seen[bal],i])
            else:
                seen[nums[i]] = i
                
        return
        