'''
2020. 09. 14
4435 - 중간계 전쟁

# 내용
중간계에 전쟁이 일어나려고 한다. 간달프는 사우론에 대항하기 위한 군대를 소집했고, 여러 종족이 이 군대에 가담했다. 전쟁을 시작하기 전에 간달프는 각 종족에 점수를 매겼다.

간달프의 군대의 각 종족의 점수는 다음과 같다.

호빗 - 1
인간 - 2
엘프 - 3
드워프 - 3
독수리 - 4
마법사 - 10

사우론의 군대의 점수는 다음과 같다.

오크 - 1
인간 - 2
워그(늑대) - 2
고블린 - 2
우럭하이 - 3
트롤 - 5
마법사 - 10
중간계는 매우 신비한 곳이어서 각 전투의 승리는 날씨, 장소, 용맹에 영향을 받지 않는다. 전투에 참여한 각 종족의 점수를 합한 뒤, 큰 쪽이 이긴다.

전투에 참여한 종족의 수가 주어졌을 때, 어느 쪽이 이기는지 구하는 프로그램을 작성하시오.

# 입력
- 첫째 줄에 전투의 개수 T가 주어진다. 각 전투는 두 줄로 이루어져 있다. 
  첫째 줄에 간달프 군대에 참여한 종족의 수가 주어진다. 
  이 값은 공백으로 구분되어 있으며, 호빗, 인간, 엘프, 드워프, 독수리, 마법사 순서이다. 둘째 줄에는 사우론 군대에 참여한 종족의 수가 주어진다. 
  이 값 역시 공백으로 구분되어 있으며, 오크, 인간, 워그, 고블린, 우럭하이, 트롤, 마법사 순서이다. 
  모든 값은 음이 아닌 정수이고, 각 군대의 점수의 합은 32비트 정수 제한을 넘지 않는다.

# 출력
- 각 전투에 대해서, "Battle"과 전투 번호를 출력한다. 
  그 다음에 간달프의 군대가 이긴다면 "Good triumphs over Evil"를, 
  사우론의 군대가 이긴다면 "Evil eradicates all trace of Good", 점수의 합이 같아 이기는 쪽이 없다면 "No victor on this battle field"를 출력한다.
'''
# 간달프 군대 점수표
Garray = [1, 2, 3, 3, 4, 10]

# 사우론 군대 점수표
Sarray = [1, 2, 2, 2, 3, 5, 10]

# 전투의 개수 T
T = int(input())

# 간달프 점수 합
Gscore = 0

# 사우론 점수 합
Sscore = 0

# 결과값을 담을 변수
result = []

for i in range(T):
    # 간달프
    G = list(map(int, input().split()))

    # 사우론
    S = list(map(int, input().split()))

    # 점수 합
    Gscore = sum([x * y for x, y in zip(Garray, G)])
    Sscore = sum([x * y for x, y in zip(Sarray, S)])
    
    # 누가 더 큰지 비교하자
    if Gscore > Sscore:
        result.append("Battle {0}: Good triumphs over Evil".format(i+1))
    elif Sscore > Gscore:
        result.append("Battle {0}: Evil eradicates all trace of Good".format(i+1))
    else:
        result.append("Battle {0}: No victor on this battle field".format(i+1))

for r in result:
    print(r)