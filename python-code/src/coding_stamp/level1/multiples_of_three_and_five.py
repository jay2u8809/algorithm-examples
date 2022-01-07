'''
    10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
    1000 미만의 자연수에서 3, 5의 배수의 총합을 구하라.
'''

result_list = list()


def solution(num1, num2):
    result = 0
    for num in range(1, 1000):
        if num % num1 == 0 or num % num2 == 0:
            result += num
            result_list.append(num)
            continue

    return result


print('Function: ', solution(3, 5))
print('List: ', sum(result_list))

one_line_resolve = sum(list(num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0))
print('One Line: ', one_line_resolve)
