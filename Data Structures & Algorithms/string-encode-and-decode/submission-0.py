class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += "".join(str(len(i))+"$"+i)
        print(encodedString)
        return encodedString
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):   # 5#Hello5#World
            j=i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : length+j+1])
            i = j+length+1
        return res
            
