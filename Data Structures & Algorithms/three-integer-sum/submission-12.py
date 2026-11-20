class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        visited = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[i], nums[l], nums[r]) not in visited:
                        visited.add((nums[i], nums[l], nums[r]))
                        result.append([nums[i], nums[l], nums[r]])
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

        return result