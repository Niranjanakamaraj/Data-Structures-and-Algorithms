class Solution:
    def combinationSum(self, candidates, target):

        ans = []
        subset = []

        def f(i, target):

            if target == 0:
                ans.append(subset.copy())
                return

            if target < 0:
                return

            for j in range(i, len(candidates)):

                subset.append(candidates[j])

                f(j, target - candidates[j])

                subset.pop()

        f(0, target)

        return ans