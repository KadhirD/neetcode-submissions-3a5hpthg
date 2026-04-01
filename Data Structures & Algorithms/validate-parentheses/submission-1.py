class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c not in hmap:
                stack.append(c)
            else:
                if stack:
                    a = stack.pop()
                    if hmap[c] == a:
                        continue
                    else:
                        return False
                else:
                    return False
        return False if stack else True



        