class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encode = str(len(s)) + "#" + s
            encoded_string.append(encode)
        
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # single encoded string -> list of strings
        result = []
        i = 0

        # iterate char by char

        while i < len(s):
            # first pos is a number 
            j = i

            # go to the first delimiter
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return result
            

