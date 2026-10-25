class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack 

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    lower_temp = stack.pop()
                    result[lower_temp] = i - lower_temp
                stack.append(i)
        
        return result

            # if stack is empty, just add it in 
            # if top of stack is larger, just add in 
            # if top of stack is smaller, calculate diff in days
