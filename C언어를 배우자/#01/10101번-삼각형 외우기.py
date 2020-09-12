'''
2020. 09. 12
10101번 - 삼각형 외우기

# 내용
삼각형의 세 각을 입력받은 다음, 
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error
를 출력하는 프로그램을 작성하시오.

# 입력
- 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.

# 출력
- 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.

'''
# 세 각을 입력받는다.
a = int(input())
b = int(input())
c = int(input())

# 세 각의 합
result = a + b + c

# 세 각의 크기가 모두 60이면
if a == 60 and b == 60 and c == 60:
  print(f"Equilateral")
# 세 각의 합이 180이고
elif result == 180:
  # 두 각이 같은 경우
  if a == b or a == c or b == c:
    print(f"Isosceles")
  # 같은 각이 없는 경우
  else:
    print(f"Scalene")
# 세 각의 합이 180이 아닌 경우
else:
  print(f"Error")