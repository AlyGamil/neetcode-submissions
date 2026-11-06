class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output = output + f"{len(s)}#{s}"
        return output

    def decode(self, s: str) -> List[str]:
        result = []
        word_length = ""
        i = 0
        while i < len(s):
            c = s[i]
            i += 1
            if c == '#':
                result.append(s[i: i + int(word_length)])
                i = i + int(word_length)
                word_length = ""
            else:
                word_length += c

        return result
    