class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack that checks if current character has duplicate, join method used to combine ending strings
        stack = []
        for c in s:
            if stack:
                if c != stack[-1]:
                    stack.append(c)
                else:
                    stack.pop()
            else:
                stack.append(c)

        return (''.join(stack))
