'''
2020. 09. 15
난이도 : 하하

1. 각 돌들이 얼마나 버틸수 있는지 배열로 주어집니다. (내구도 0까지는 독의 몸무게를 버틸 수 있습니다. 0미만이 되면 독은 살아남지 못합니다.)

2. 각 독들의 개인정보가 JSON(JSON은 큰 따옴표로 묶여야 합니다. 
**가능하다면 json을 import하여 풀어보세요!**)으로 주어집니다. 개인정보는 보호되지 않습니다.

3. 각 돌에 독들이 착지할 때 돌의 내구도는 몸무게만큼 줄어듭니다.
    ex) [1,2,1,4] 각 돌마다 몸무게 1인 독 1마리 2마리 1마리 4마리의 착지를 버틸 수 있습니다.

4. 독들의 점프력이 각자 다릅니다. 
    ex) 점프력이 2라면 2칸씩 점프하여 착지합니다.

5. 각 독들은 순서대로만 다리를 건넙니다.
돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

출력
생존자 : ['씨-독']

입력
돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

출력
생존자 : ['루비독', '씨-독']
'''

import json
돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

JSON독 = json.dumps(독, ensure_ascii=False)
JSON독 = json.loads(JSON독)
print(JSON독[0])

# remove -> O(n)
# del -> O(1) best!
def 징검다리를건너라(돌의내구도, 독):
  #answer = [독[i]['이름'] for i in range(len(독))]
  answer = [i['이름'] for i in 독]
  
  for i in 독:
    독의위치 = 0
    while 독의위치 < len(돌의내구도)-1:
      독의위치 += int(i['점프력'])
      돌의내구도[독의위치-1] -= int(i['몸무게'])
      if 돌의내구도[독의위치-1] < 0:
        del answer[answer.index(i['이름'])]
        break
  return answer

print(징검다리를건너라(돌의내구도, 독))

# List는 주소값을 전달하기 때문에 값을 직접 변경이 가능하다.
#l = [1, 2, 3, 4, 5]
#def change(l):
#  l[0] = 1000
#change(ll)