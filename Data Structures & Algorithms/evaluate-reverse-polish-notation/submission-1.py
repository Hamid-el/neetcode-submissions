class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(token1, token2, ar):
            if ar == "+":
                return token1 + token2
            elif ar == "-":
                return token2 - token1 # switched order
            elif ar == "*":
                return token1 * token2
            else:
                return int(token2 / token1) # switched order

        stack = []
        for t in tokens:
            if t != "+" and t != "-" and t != "*" and t != "/":
                stack.append(int(t))
            else:
                val = eval(stack[-1], stack[-2], t)
                stack.pop()
                stack.pop()
                stack.append(val)
        
        return stack[0]