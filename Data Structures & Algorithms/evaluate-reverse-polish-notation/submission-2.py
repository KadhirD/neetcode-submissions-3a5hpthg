class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i == "+" :
                res = stack.pop()+stack.pop()
                stack.append(res)
            elif i == '-' :
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '*' :
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                res = b/a
                stack.append(int(res))
            else : 
                stack.append(int(i))
        return stack[0]
        
        