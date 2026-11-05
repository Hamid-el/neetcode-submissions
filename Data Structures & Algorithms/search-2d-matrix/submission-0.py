class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = -1
        while l <= r:
            mid = (r + l) // 2
            if matrix[mid][0] <= target:
                l = mid + 1
                row = mid # kann sein wir an target row vorbei gehen, aber egal wir speichern ja 
            else: 
                r = mid - 1 
        
        if row == -1:
            return False
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return False # first bin only catches where target would be, not whether it actually is in there