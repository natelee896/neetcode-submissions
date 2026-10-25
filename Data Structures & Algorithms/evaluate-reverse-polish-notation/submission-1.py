class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stacks for the numbers, operations cause pops 

        ops = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                rightSide = stack.pop()
                leftSide = stack.pop()

                if token == ops[0]:
                    stack.append(leftSide + rightSide)
                elif token == ops[1]:
                    stack.append(leftSide - rightSide)
                elif token == ops[2]:
                    stack.append(leftSide * rightSide)
                elif token == ops[3]:
                    stack.append(int(leftSide / rightSide))
        
        return stack[-1]
