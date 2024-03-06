class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        # dictionary to store pairs for cross referencing
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            # if character is opening bracket add to stack
            if c in '({[':
                stack.append(c)
            else:
                if stack:
                    if pairs[c] != stack.pop():
                        return False
                else:
                    return False

        return len(stack) == 0

        # same concept of adding opening brackets to stack, but no cross referencing with map

        # for p in s:
        #     if p == '(':
        #         stack.append('(')
        #     elif p == '[':
        #         stack.append('[')
        #     elif p == '{':
        #         stack.append('{')
        #     elif p == ')':
        #         if stack:
        #             if stack.pop() != '(':
        #                 return False
        #         else:
        #             return False
        #     elif p == ']':
        #         if stack:
        #             if stack.pop() != "[":
        #                 return False
        #         else:
        #             return False
        #     elif p == '}':
        #         if stack:
        #             if stack.pop() != '{':
        #                 return False
        #         else:
        #             return False

        # if stack:
        #     return False

        # return True


