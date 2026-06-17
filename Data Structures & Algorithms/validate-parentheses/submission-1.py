class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{':'}','[':']','(':')','<':'>'}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != i:
                    return False
        if len(stack) == 0:
            return True
        return False