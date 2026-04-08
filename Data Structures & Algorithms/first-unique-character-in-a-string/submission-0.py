class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {} # char: count
        firstUniq = None

        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1

        for k, v in counter.items():
            if v > 1:
                continue
            firstUniq = s.index(k)
            break

        return firstUniq if firstUniq is not None else -1