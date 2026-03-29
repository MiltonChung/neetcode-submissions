class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {} # sortedWord -> res index
        res = []
        i = 0

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in chars:
                res[chars[sortedWord]].append(word)
            else:
                chars[sortedWord] = i
                res.append([word])
                i += 1

        return res
        


