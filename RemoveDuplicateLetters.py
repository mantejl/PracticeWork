class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # map to determine where the furthest index of character
        lex_order = {}
        # stack to check previous letter and see if it's the latest possible character available
        stack = []
        # set to have quick lookup: O(1)
        visited = set()

        # creating map to store latest character index
        for i in range(len(s)):
            lex_order[s[i]] = i

        for i in range(len(s)):
            # if we have alr seen this character, we can skip it
            if s[i] in visited:
                continue

                # if stack is available and the top of the stack (our string so far)
            # is greater than the element we're adding and if we can add this element
            # later down the line
            while stack and stack[-1] > s[i] and i < lex_order[stack[-1]]:
                # we remove it from our stack and visited set
                visited.remove(stack[-1])
                stack.pop()

            # then add the char to our stack and visited list
            stack.append(s[i])
            visited.add(s[i])

        # return our joined stack
        return "".join(stack)


