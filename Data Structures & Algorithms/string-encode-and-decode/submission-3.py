class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            encoded = str(len(word)) + '#' + word
            result.append(encoded)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        number = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result
