class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        if k == len(nums_set):
            return list(nums_set)

        table = defaultdict(int)
        for i in nums:
            table[i] = 1 + table[i]

        return sorted(table, key=table.get)[-k:]