class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq = Counter(s1)
        need = len(freq)
        for i in range(len(s2)):
            count = {}
            curr = 0

            for j in range(i, len(s2)):
                count[s2[j]] = count.get(s2[j], 0) + 1

                if freq.get(s2[j], 0) < count[s2[j]]:
                    break
                if freq.get(s2[j], 0) == count[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
        
        return False
