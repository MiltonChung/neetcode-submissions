class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i1, i2 = len(a) - 1, len(b) - 1
        n = max(i1, i2)
        carry = 0
        res = []

        while i1 >= 0 or i2 >= 0 or carry > 0:
            val1 = int(a[i1]) if i1 >= 0 else 0
            val2 = int(b[i2]) if i2 >= 0 else 0

            total = val1 ^ val2 ^ carry
            # if carry == 1:
            #     total = total ^ carry

            # if (val1 == 1 and val2 == 1) or (val1 == 1 and carry == 1) or (carry == 1 and val2 == 1):
            if val1 + val2 + carry >= 2:
                carry = 1
            else:
                carry = 0
            
            res.append(str(total))

            i1 -= 1
            i2 -= 1

        res.reverse()
        return "".join(res)
