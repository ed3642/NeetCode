class Solution:
    def __init__(self) -> None:
        self.rows = [[1], [1, 1]]

    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        prev_row = None
        if len(self.rows) > rowIndex:
            prev_row = self.rows[rowIndex]
        else:
            prev_row = self.getRow(rowIndex - 1)

        ans = [1]
        for i in range(rowIndex - 1):
            ans.append(prev_row[i] + prev_row[i + 1])
        ans.append(1)

        return ans