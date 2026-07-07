def subset_sum(arr, target):
    def dfs(i, s):
        if s == target:
            return True
        if i == len(arr) or s > target:
            return False
        return dfs(i + 1, s + arr[i]) or dfs(i + 1, s)
    return dfs(0, 0)