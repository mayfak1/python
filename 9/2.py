from random import choice
m = [[0 for i in range(3)]for h in range(3)]

f=False
while not f:
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            m[i][j] = choice(number)
            number.remove(m[i][j])

    f = True
    magic_sum = sum(m[0])

    for i in range(3):
        if sum(m[i]) != magic_sum:
            f = False
            break
    for j in range(3):
        stolb_sum = m[0][j] + m[1][j] + m[2][j]
        if stolb_sum != magic_sum:
            f = False
            break

    diagonal_sum1 = m[0][0] + m[1][1] + m[2][2]
    diagonal_sum2 = m[0][2] + m[1][1] + m[2][0]
    if diagonal_sum1 != magic_sum or diagonal_sum2 != magic_sum:
        f = False

print("Магический квадрат:")
for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()