'''
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제 입력 1
5
예제 출력 1
*
**
***
****
*****
'''

import sys

N = list(map(int,sys.stdin.readline().split()))

for i in range(N[0]):
    # stars=''
    # for j in range(i+1):
    #     stars = stars+'*'
    # print(stars)

    print(f"{'*'*(i+1)}")

# ------------------------------------------------------------------------------------------------------------------정리
# print(f"{}") 사용법
# https://docs.python.org/ko/3/tutorial/inputoutput.html
