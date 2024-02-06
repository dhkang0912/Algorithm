t = int(input())
stone_div = t // 3
stone = t % 3

if stone_div % 2 == 0:
    person = [1, 0]
    while stone >= 0:
        stone = stone - 1
        person[0] = not person[0]
        person[1] = not person[1]
else:
    person = [0,1]
    while stone >= 0:
        stone = stone - 1
        person[0] = not person[0]
        person[1] = not person[1]
if person[0]:
    print('CY')
else:
    print('SK')