class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(",
                "]": "[",
                "}": "{"
        }
        
        for i in range(len(s)):
           # or s[i] not in pair = oben paren
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if not stack or stack[-1]  != pair[s[i]]:
                    return False
                    
                stack.pop()
            
            
        
        return stack == []
        