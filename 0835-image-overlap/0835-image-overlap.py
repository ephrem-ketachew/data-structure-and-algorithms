class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def count_overlap() -> int:
            count = 0
            for i in range(n):
                for j in range(n):
                    if img1[i][j] == img2[i][j] == 1:
                        count += 1
            return count

        def move_left():
            maxx = 0
            for _ in range(n):
                for j in range(n - 1, -1, -1):
                    if j == 0:
                        for i in range(n):
                            img1[i][j] = 0
                    else:
                        for i in range(n):
                            img1[i][j] = img1[i][j - 1]
                maxx = max(maxx, count_overlap())
            return maxx

        def move_right():
            maxx = 0
            for _ in range(n):
                for j in range(n):
                    if j == n - 1:
                        for i in range(n):
                            img1[i][j] = 0
                    else:
                        for i in range(n):
                            img1[i][j] = img1[i][j + 1]
                maxx = max(maxx, count_overlap())
            return maxx

        original = [img1[i][:] for i in range(n)]
        max_overlap = count_overlap()

        max_overlap = max(max_overlap, move_left())
        img1 = [original[i][:] for i in range(n)]
        max_overlap = max(max_overlap, move_right())
        img1 = [original[i][:] for i in range(n)]

        for _ in range(n):
            for i in range(n - 1, -1, -1):
                if i == 0:
                    for j in range(n):
                        img1[i][j] = 0
                else:
                    for j in range(n):
                        img1[i][j] = img1[i - 1][j]
            
            img = [img1[i][:] for i in range(n)]

            max_overlap = max(max_overlap, count_overlap())

            max_overlap = max(max_overlap, move_left())
            
            img1 = [img[i][:] for i in range(n)]
            max_overlap = max(max_overlap, move_right())

            img1 = [img[i][:] for i in range(n)]

        img1 = [original[i][:] for i in range(n)]
        for _ in range(n):
            for i in range(n):
                if i == n - 1:
                    for j in range(n):
                        img1[i][j] = 0
                else:
                    for j in range(n):
                        img1[i][j] = img1[i + 1][j]
            
            img = [img1[i][:] for i in range(n)]

            max_overlap = max(max_overlap, count_overlap())

            max_overlap = max(max_overlap, move_left())
            
            img1 = [img[i][:] for i in range(n)]
            max_overlap = max(max_overlap, move_right())

            img1 = [img[i][:] for i in range(n)]

        return max_overlap
