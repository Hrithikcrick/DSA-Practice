class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        arr = []

        for i in range(len(s)):

            if s[i] == "*":
                if length > 0:
                    length -= 1

            elif s[i] == "#":
                length = length * 2

            elif s[i] == "%":
                length = length

            else:
                length += 1

            arr.append(length)

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            prev = arr[i - 1] if i > 0 else 0

            if s[i] == "*":
                length = prev

            elif s[i] == "#":
                if k >= prev:
                    k -= prev
                length = prev

            elif s[i] == "%":
                k = prev - 1 - k
                length = prev

            else:
                if k == prev:
                    return s[i]
                length = prev

        return '.'
