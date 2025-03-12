class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        ans = [[1],[1,1]]
        for i in range(rowIndex-2+1):
            val = [1]
            for j in range(len(ans[-1]) - 1):
                val.append(ans[-1][j] + ans[-1][j + 1])
            val.append(1)
            ans.append(val)
        return ans[-1]
        
        
        
        