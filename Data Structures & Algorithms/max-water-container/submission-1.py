class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        calculate_area = lambda l1, r1: (r1 - l1) * int(min(heights[l1], heights[r1]))
        max_area = (r - l) * int(min(heights[l], heights[r]))
        while l < r:
            move_l = l + 1
            move_r = r - 1
            if calculate_area(l, move_r) > max_area:
                r = move_r
                max_area = calculate_area(l, move_r)
            elif calculate_area(move_l, r) > max_area:
                l = move_l
                max_area = calculate_area(move_l, r)
            elif heights[move_l] < heights[move_r]:
                l = move_l
            else:
                r = move_r
        return max_area