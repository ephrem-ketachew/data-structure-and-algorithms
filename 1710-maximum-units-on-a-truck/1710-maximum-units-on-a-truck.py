class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        max_units = 0
        size = 0
        for n, u in boxTypes:
            if size + n <= truckSize:
                max_units += n * u
                size += n
            else:
                m = truckSize - size
                max_units += m * u
                break

        return max_units