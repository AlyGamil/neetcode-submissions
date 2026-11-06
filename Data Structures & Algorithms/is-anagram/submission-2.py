class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        return s_list == t_list