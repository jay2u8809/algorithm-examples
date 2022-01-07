"""
    디지털 시계에서 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초인가?
    > 00:00
      00:01
      00:02
      ...
      23:59
"""


def calcSecondsAppeardThree(day):
    result = 0
    for day in range(day):
        for hour in range(0, 24):
            for minute in range(0, 60):
                # 03:13, 13:23, 23:33 ...
                if str(hour).find('3') != -1 or '3' in str(minute):
                    result += 1
    return result * 60


print(calcSecondsAppeardThree(1))
