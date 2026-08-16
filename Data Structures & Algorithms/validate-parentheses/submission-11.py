class Solution:
    def isValid(self, s: str) -> bool:
        mapBracket = {"}": "{", ")": "(", "]":"["}
        stack = []

        for b in s:
            if b in mapBracket.values():
                stack.append(b)
            else:
                if not stack:
                    return False
                if stack[-1] != mapBracket[b]:
                    return False
                stack.pop()
        
        return True if len(stack) == 0 else False
        