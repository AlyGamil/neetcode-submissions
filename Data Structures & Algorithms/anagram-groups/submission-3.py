class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        place_holder = {}

        for i, substring in enumerate(strs):
            substring_sorted = "".join(sorted(substring))
            if substring_sorted in place_holder:
                place_holder[substring_sorted].append(substring)
                continue
            place_holder[substring_sorted] = [substring]

        return list(place_holder.values())