class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = 0
        while r < len(nums):
            if r == l:
                r += 1
                continue
            if nums[l] + nums[r] == target:
                return [l, r]

            r += 1
            if r == len(nums):
                l += 1
                r = l

        return []