'''
문제
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자.
단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다.
BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다.
테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 이 글에 설명되어 있다.

이 블로그 글에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.

입력
첫 줄에 테스트케이스의 개수 T가 주어진다.
T는 최대 1,000,000이다.
다음 T줄에는 각각 두 정수 A와 B가 주어진다.
A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

예제 입력 1
5
1 1
12 34
5 500
40 60
1000 1000
예제 출력 1
2
46
505
100
2000
'''

import sys

T = int(input())
for i in range(T):
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(a[0]+a[1])


# -------------------------------------------------------------------------------------------------------------------정리

# import sys

# 1. sys.stdin.readline()

# 이 메소드는 입력한 한 라인을 interable한 컨테이너에 저장한다.
# for x in sys.stdin.readline():
#     print(x)
# **input
# 12 3 4 5
# **output
# 12
# 3
# 4
# 5
# 1
# 2
#
# 3
#
# 4
#
# 5

# 띄어쓰기와 \n까지 포함하므로 split()을 이용하는 것이 좋다.
# for x in sys.stdin.readline().split():
#     print(x)

# **input
# 12 3 4 5
# **output
# 12
# 3
# 4
# 5

# 2. sys.stdin

# 여러 줄을 입력받고 싶으면 sys.stdin을 이용하는 것이 좋다.
# for line in sys.stdin:
#     print(line)
#
# 11
# 11
#
# 22
# 22
#
# 51
# 51

# 입력 받은 값 리스트로 저장하기
# a = list(map(int,sys.stdin.readline().split()))
# print(a)
#
# 1 2 3
# [1, 2, 3]

# 여러줄 입력 받은 값 저장하기
# sys.stdin은 ^Z를 입력받으면 종료해주기 때문에 임의의 여러 줄을 입력받아야 하는 문제에서 좋음.
# input_list = []
# for line in sys.stdin:
#     input_list.append(tuple(map(int,line.strip().split())))
#     print(input_list)
#
# 1 1
# [(1, 1)]
# 2 2
# [(1, 1), (2, 2)]
# 3 3
# [(1, 1), (2, 2), (3, 3)]
# 5 1
# [(1, 1), (2, 2), (3, 3), (5, 1)]

