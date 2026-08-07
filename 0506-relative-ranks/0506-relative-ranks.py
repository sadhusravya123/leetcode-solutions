class Solution(object):
    def findRelativeRanks(self, score):
        ans = [""] * len(score)
        order = sorted(range(len(score)), key=lambda i: score[i], reverse=True)

        for i in range(len(order)):
            if i == 0:
                ans[order[i]] = "Gold Medal"
            elif i == 1:
                ans[order[i]] = "Silver Medal"
            elif i == 2:
                ans[order[i]] = "Bronze Medal"
            else:
                ans[order[i]] = str(i + 1)

        return ans
        