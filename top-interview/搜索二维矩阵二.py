"""
2021年1月6日
从二维矩阵中找到指定元素位置(二维矩阵总是从左到右升序，从上到下升序)

方案：
1.从对角线元素利用二分法搜索
2.将二维矩阵切分成更小矩阵，根据矩阵内最大元素选择性搜索
3.滑动二分法，从最坐下坐标开始，小于则往右移，大于往上移，知道找到
3.暴力
"""

input1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
args1 = 5

input2 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
args2 = 20


def a():
    def search_matrix(matrix, target):
        col_len = len(matrix[0]) - 1
        row_len = len(matrix) - 1
        row_start = 0
        while row_start < row_len or col_len > -1:
            col_len_ = col_len if col_len > -1 else 0
            row_start = row_start if row_start < row_len else row_len
            if matrix[row_start][col_len_] == target:
                return [row_start, col_len_]
            if matrix[row_start][col_len_] < target:
                i = row_start
                while i <= row_len:
                    if matrix[i][col_len_] == target:
                        return [i, col_len_]
                    i += 1
            else:
                i = col_len_
                while i >= 0:
                    if matrix[row_start][i] == target:
                        return [row_start, i]
                    i -= 1
            row_start += 1
            col_len -= 1

    def search_matrix(matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return [row, col]

        return False

    return search_matrix(
        input1, args1)


print(a())
