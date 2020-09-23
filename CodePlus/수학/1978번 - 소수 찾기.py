'''
2020. 09. 24
1978번 - 소수 찾기 

# 내용
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
- 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
- 주어진 수들 중 소수의 개수를 출력한다.
'''

# input
N = int(input())
num = list(map(int, input().split()))
count = 0
global j


# 소수 구하기
def prime(n):
    j = 2
    if n < 2:
        return False

    while j*j <= n:
        if n % j == 0:
            return False
        j += 1
    return True


# for loop
for i in range(N):
    if prime(num[i]):
        count += 1

# output
print(count)
