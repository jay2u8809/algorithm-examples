"""
    > 탭을 공백 문자로 바꾸기
    소스 코드 내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오
"""

import os


# f = open('./sample/sample_convert.py', 'r', encoding='UTF8')
# read_data = f.read()
# f.close()
# print(read_data.replace('   ', 'space'))

def fileTap2Space(fname):
    with open(fname, 'r', encoding='UTF8') as f:
        data = f.read()
        data = data.replace('   ', 'ssss')
    with open(fname, 'w', encoding='UTF8') as f:
        f.write(data)
    return data


print(fileTap2Space('./sample/sample_convert.py'))

# 특정 경로 내의 파일 읽어오기
for root, dirs, files in os.walk(''):
    for file in files:
        if file.endswith('.py'):  # 특정 확장자만 검출
            print(root + '¥' + file)
