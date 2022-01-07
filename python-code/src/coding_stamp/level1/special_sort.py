"""
   n 개의 정수를 가진 배열이 존재, 양/음의 정수를 모두 가진다
   이 배열의 값을 정렬하되 음의 정수는 앞쪽, 양의 정수는 뒷쪽에 있어야 한다.
   또한, 양의 정수와 음의 정수의 순서에는 변화가 없어야 한다.

   > origin: -1 1 3 -2 2
   > sorted: -1 -2 1 3 2
"""


def specialSortedArr(arr):
    minusArr = []
    plusArr = []
    for num in arr:
        minusArr.append(num) if num < 0 else plusArr.append(num)
    return minusArr + plusArr


dummy = [-1, 1, 3, -2, 2]
print(specialSortedArr(dummy))

dummyLong = [-1, 1, 3, -2, 2, 0, 13, -33, 65, 76, 45, 343, -32, -54432, 432, 0, -43, 32, 43, -4234, -987]
print(specialSortedArr(dummyLong))