num_1 = int(input())
num_2 = int(input())

first_digit = num_2 % 10
second_digit = (num_2//10) % 10
third_digit = (num_2//100) % 1000

first_line = first_digit * num_1
second_line = second_digit * num_1
third_line = third_digit * num_1
sumV = first_line + (second_line*10) + (third_line*100)

print(first_line)
print(second_line)
print(third_line)
print(sumV)