class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not monoStack:
                monoStack.append(i)
            else:
                while monoStack and temp > temperatures[monoStack[-1]]:
                    lower_temp = monoStack.pop()
                    result[lower_temp] = i - lower_temp
                monoStack.append(i)
        
        return result