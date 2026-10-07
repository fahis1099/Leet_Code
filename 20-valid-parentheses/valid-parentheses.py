class Solution:
    def isValid(self, s: str) -> bool:
        Matching = True
        stack = []
        for i in s:
            if i in ['{','(','[']:
                stack.append(i)
            elif len(stack) != 0:
                if stack[-1] == "{" and i == "}":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "(" and i == ")":
                    stack.pop()
                else:
                    Matching = False
                    break
            else:
                Matching = False
                break

        if Matching and len(stack) == 0:
            return True
        else:
            return False