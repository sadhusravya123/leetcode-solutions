class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            ans += chr(ord('z') - (total % 26))

        return ans
        