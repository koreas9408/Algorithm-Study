'''
섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)
'''
text = [
    '   + -- + - + -   ',
    '   + --- + - +   ',
    '   + -- + - + -   ',
    '   + - + - + - +   '
    ]
# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자
# join(enumerate) : list 를 하나의 문자열로
# replace('old', 'new')
# 연속해서 replace를 사용할 수 있다.

# zfill() -> 자리 수를 맞춰준다.
# map(function, enumerate)

l = []
for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# 리스트 컴프리헨션
print([i for i in range(10) if i % 2 == 0])

print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)])