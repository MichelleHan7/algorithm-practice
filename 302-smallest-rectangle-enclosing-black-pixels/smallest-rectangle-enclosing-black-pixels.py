class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left = 0
        right = y-1
        while left <= right:
            mid = (left + right) // 2
            if any(image[i][mid] == '1' for i in range(m)):
                right = mid - 1
            else:
                left = mid + 1
        minCol = left

        left = y
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if any(image[i][mid] == '1' for i in range(m)):
                left = mid + 1
            else:
                right = mid - 1
        maxCol = left

        top, bottom = 0, x
        while top < bottom:
            mid = (top + bottom) // 2
            if "1" in image[mid]:
                bottom = mid
            else:
                top = mid + 1
        minRow = top

        # Find the first row containing no black pixels
        top, bottom = x, m
        while top < bottom:
            mid = (top + bottom) // 2
            if "1" in image[mid]:
                top = mid + 1
            else:
                bottom = mid
        maxRow = top

        return (maxRow - minRow) * (maxCol - minCol)
