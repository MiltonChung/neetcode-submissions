class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # sortedWord -> [string]
        res = []

        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString not in hashmap:
                hashmap[sortedString] = []
            hashmap[sortedString].append(s)
        
        for k, _ in hashmap.items():
            res.append(hashmap[k])
        return res