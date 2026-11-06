class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        sequences = dict.fromkeys(nums, 1)
        longest_consecutive = 1
        for i in range(len(nums)):
            if nums[i] - 1 in sequences:
                sequences[nums[i]] = sequences[nums[i] - 1] + 1
                longest_consecutive = sequences[nums[i]] \
                    if sequences[nums[i]] > longest_consecutive else longest_consecutive
            else:
                sequences[nums[i]] = 1

        return longest_consecutive