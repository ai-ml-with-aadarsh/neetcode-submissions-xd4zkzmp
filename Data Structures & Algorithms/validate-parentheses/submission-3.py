class Solution:
    def isValid(self, s: str) -> bool:
        res = False
        stack = list()
        pair = ['()', '{}', '[]']

        s = list(s)
        len_s = len(s)

        if len_s and len_s % 2 == 0:
            for bc in s:
                if bc in '({[':
                    stack.append(bc)
                elif not stack or stack.pop() + bc not in pair:
                    return False

            res = not stack

        return res