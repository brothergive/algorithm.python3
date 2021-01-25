'''
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.
'''

# input().split() : split의 default는 공백이다.
i1,i2 = input().split()
print(int(i1)+int(i2))


# # int(input())
# i1 = int(input())
# i2 = int(input())
# print(i1+i2)

# # eval(input())
# i1 = eval(input())
# i2 = eval(input())
# print((i1+i2))

