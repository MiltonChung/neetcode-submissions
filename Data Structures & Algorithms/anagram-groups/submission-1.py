class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # sortedWord -> [string]
        res = []

        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString in hashmap:
                hashmap[sortedString].append(s)
            else:
                hashmap[sortedString] = [s]
        
        for k, _ in hashmap.items():
            res.append(hashmap[k])
        return res