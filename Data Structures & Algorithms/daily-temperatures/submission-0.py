class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp,index
        res = [0]*len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and n>stack[-1][0]:
                a,b = stack.pop()
                res[b] = i - b
            stack.append([n,i])
        return res