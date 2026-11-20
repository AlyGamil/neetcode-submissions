class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left_height, max_right_height = height[0], height[-1]
        water_amount = 0
        while l < r:
            if max_left_height < max_right_height:
                l += 1
                max_left_height = max(height[l], max_left_height)
                if height[l] < max_left_height:
                    water_amount += min(max_left_height, max_right_height) - height[l]
            else:
                r -= 1
                max_right_height = max(height[r], max_right_height)
                if height[r] < max_right_height:
                    water_amount += min(max_left_height, max_right_height) - height[r]
        return water_amount