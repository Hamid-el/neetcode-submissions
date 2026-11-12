class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):  # right path/child
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] + total > target:
                    break
                
                subset.append(candidates[j])
                dfs(j+1, total + candidates[j]) # j+1 instead of j to skip same number,left path/child in tree
                subset.pop()

        dfs(0, 0)
        return res