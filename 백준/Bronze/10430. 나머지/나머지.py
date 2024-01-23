input = list(map(int, input().split()))
A = input[0]
B = input[1]
C = input[2]
result_1 = int((A + B) % C)
result_2 = int(((A % C) + (B % C)) % C)
result_3 = int((A * B) % C)
result_4 = int(((A % C) * (B % C)) % C)

print(result_1)
print(result_2)
print(result_3)
print(result_4)