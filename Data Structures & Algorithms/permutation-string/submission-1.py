class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if count == window:
            return True
        for i in range(len(s1),len(s2)):
            window[s2[i]]+=1
            window[s2[i-len(s1)]]-=1
            if count == window:
                return True 
        return False

        