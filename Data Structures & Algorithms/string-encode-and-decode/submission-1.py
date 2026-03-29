class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder = '*'
        encoded = ''

        for s in strs:
            length = len(s)
            encoded += f"{length}{encoder}{s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # length = 0
            # word = ''
            # if s[i] == '*':
            #     length = int(s[i-1])
            #     if not length: continue
            #     i += 1
            #     for j in range(i, i + length):
            #         word += s[j]
            #     res.append(word)
            #     i += length
            # i += 1
            j = i
            while s[j] != '*':
                j += 1
            num = int(s[i:j])
            i = j + 1
            word = s[i:i+num]
            res.append(word)
            i += num
        
        return res


