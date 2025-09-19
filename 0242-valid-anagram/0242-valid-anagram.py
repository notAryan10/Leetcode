class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for char in s:
             count[ord(char) - ord('a')] += 1
        for char in t:
             count[ord(char) - ord('a')] -= 1
        return all(c == 0 for c in count)
