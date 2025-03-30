class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(matrix,target):
            index = -1
            left = 0
            right = len(matrix) - 1
            while left <= right:
                mid = left + (right - left )// 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        index = findRow(matrix,target)
        left , right = 0 , len(matrix[index]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


        