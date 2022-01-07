"""
    [실행순서]
    1. 입력할 정수의 갯수를 입력
    2. 1.에서 입력받은 갯수만큼 정수를 입력
    3. 2.에서 입력받은 정수들의 합과 평균값을 출력
    4. 할당된 메모리 공간을 비움

    [요구사항]
    1. 메모리 공간은 사용자의 입력 수에 따라 가변적
    2. 사용한 공간은 마지막에 비워야함
    3. 배열을 사용하지 않음
"""

cnt = n = int(input('Input Num: '))
result = 0
while 0 < cnt:
    result += int(input('Num: '))
    cnt -= 1

print('RESULT: {}, {}'.format(result, result / n))

# del n, result, cnt
