class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            anagram = "".join(sorted(word))
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(word)
        
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        
        return result