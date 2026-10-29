class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        r1, c1, r2, c2 = rec2
        point1, point2 = sorted([(x1, x2), (r1, r2)])
        a, b = point1
        c, d = point2
        point1, point2 = sorted([(y1, y2), (c1, c2)])
        e, f = point1
        g, h = point2
        return b > c and f > g