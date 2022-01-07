"""
    게시물의 총 건수와 1 페이지에 보여줄 게시물 수를 입력으로 주었을 때, 총 페이지 수를 리턴하라
    > 입력: 총 건수(m), 1 페이지에 보여줄 게시물 수(n), 단 1 <= n
    > 출력: 총 페이지 수

    m  | n  | 출력
    0  | 1  | 0
    1  | 1  | 1
    2  | 1  | 2
    1  | 10 | 1
    10 | 10 | 1
    11 | 10 | 2
"""

import math


def calcTotalPage(total, num):
    # return math.ceil(total / num)
    result = total // num
    return result if total % num == 0 else result + 1


print(calcTotalPage(0, 1))
print(calcTotalPage(1, 1))
print(calcTotalPage(2, 1))
print(calcTotalPage(1, 10))
print(calcTotalPage(10, 10))
print(calcTotalPage(11, 10))
