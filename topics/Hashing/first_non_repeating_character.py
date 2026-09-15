class Solution:
    def firstNonRepeatingCharacter(self, text: str) -> str:
        freq = {}

        for c in text:
            freq[c] = freq.get(c, 0) + 1

        for c in text:
            if freq[c] == 1:
                return c

        return ""
