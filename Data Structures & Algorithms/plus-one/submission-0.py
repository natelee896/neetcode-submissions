class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [str(i) for i in digits]

        full = int("".join(result)) + 1

        output = []

        while full:
            output.append(full % 10)
            full //= 10
        
        output.reverse()
        return output

            