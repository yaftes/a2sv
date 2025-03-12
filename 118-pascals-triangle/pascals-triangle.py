class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]

        for i in range(numRows-2):
            val = [1]
            for j in range(len(ans[-1]) - 1):
                val.append(ans[-1][j] + ans[-1][j + 1])
            val.append(1)
            ans.append(val)
        return ans


        