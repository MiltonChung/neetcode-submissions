class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            sortedWord = ''.join(sorted(list(word)))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = []
            hashmap[sortedWord].append(word)
        
        return list(hashmap.values())