class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = right = 0
        longest_substring = 0
        while right < len(s):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            longest_substring = max(longest_substring, mp[s[right]] - mp[s[left]] + 1)
            right += 1

        return longest_substring