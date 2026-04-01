class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #{1:1,2:2,3:3}
        for i in nums:
            count[i] = 1+count.get(i,0)
        
        ListS = [] 
        for n, freq in count.items():
            ListS.append([freq,n])
        ListS.sort()
        
        Res = []
        for l in range(k):
            element = ListS.pop()
            value = element[1]
            Res.append(value)
        return Res






        