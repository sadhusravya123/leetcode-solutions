class Solution(object):
    def backspaceCompare(self, s, t):
        def build(x):
            stack = []
            for ch in x:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)