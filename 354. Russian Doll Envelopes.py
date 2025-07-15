class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # [[2,3],[5,4],[6,4],[6,7]]
        # [3,4,7]
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        dp = []

        for w, h in env:
            i = bisect_left(dp, h)

            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)