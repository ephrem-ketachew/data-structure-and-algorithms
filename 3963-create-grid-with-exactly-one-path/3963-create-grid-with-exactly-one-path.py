class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        row = '.' + '#' * (n - 1)
        grid = [row for _ in range(m - 1)]
        grid.append('.' * n)
        return grid