class Solution:
    def isPalindrome(self, s: s) -> bool:
        left = 0
        right = len(s)-1
        formatted_sing = []

        while left < right :
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -=1
            elif (s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else : return False
        return True    

        
        