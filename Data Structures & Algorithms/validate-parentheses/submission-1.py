class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paran in s:
            if paran == "(" or paran == "[" or paran == '{':
                stack.append(paran)
            else:
                if stack and stack[-1] == "(" and paran == ")":
                    stack.pop()
                elif stack and stack[-1] == "[" and paran == "]":
                    stack.pop()
                elif stack and stack[-1] == "{" and paran == "}":
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                