# 15. Формируется матрица F следующим образом:
# если в Е количество чисел, больших К в четных столбцах в области 1 больше,
# чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами,
# иначе В и С поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: A*F– K*A^T.
# Выводятся по мере формирования А, F и все матричные операции последовательно.

from random import randint

print('Введите N:', end=' ')
n = int(int(input()))
print('Введите K:', end=' ')
k = int(int(input()))
# массивы и матрицы для задания
F = []
Atrans = []
Raz = []
Proizv = []
p = 0  # переменная которая следит за нечётностью
kol = 0  # числа, большие К в четных столбцах в области 1
chisl = 0  # сумма чисел в нечетных строках в области 3
nado = 0
# заполнение и создание основной матрицы
for i in range(n):  # создание матриц
    F.append([0] * n)
    Atrans.append([0] * n)
    Raz.append([0] * n)
    Proizv.append([0] * n)
print('Основная матрица')
for i in range(len(F)):  # вывод основной
    for j in range(len(F)):
        F[i][j] = randint(-10, 10)
        print("{:4d}".format(F[i][j]), end="")
    print()
print()
A = F
if (n / 2) % 2 != 0:  # подсчёт по условию
    p += 1  # нечётность
    for i in range(n // 2 + 1, n // 2 + n // 4 + 2):  # рассматриваем 1 область
        for j in range(n // 2 + 1, n // 2 + n // 4 + 2):
            if i >= j and j % 2 == 0 and F[i][j] > k:
                kol += 1
    for i in range(n // 2 + n // 4 + 2, n):  # рассматриваем 1 область
        for j in range(n // 2 + 1, n // 2 + n // 4 + 1):
            if j % 2 == 0 and i <= n - (j - n // 2) and F[i][j] > k:
                kol += 1
    for i in range(n // 2 + 1, n // 2 + n // 4 + 2):  # рассматриваем 3 область
        for j in range(n // 2 + n // 4 + 1, n):
            if i % 2 == 0 and i >= n - (j - n // 2):
                chisl += 1
    for i in range(n // 2 + n // 4 + 2, n):  # рассматриваем 3 область
        for j in range(n // 2 + n // 4 + 1, n):
            if i % 2 == 0 and i <= j:
                chisl += 1
elif n % 2 == 0 and n % 4 == 0:  # подсчёт по условию
    for i in range(n // 2 + 1, n // 2 + n // 4):  # рассматриваем 1 область
        for j in range(n // 2 + 1, n // 2 + n // 4):
            if j % 2 != 0 and i >= j and F[i][j] > k:
                kol += 1
    print('')
    for i in range(n // 2 + n // 4 + 1, n):  # рассматриваем 1 область
        for j in range(n // 2 + 1, n // 2 + n // 4):
            if j % 2 != 0 and i <= n - (j - n // 2) and F[i][j] > k:
                kol += 1
    for i in range(n // 2, n // 2 + n // 4):  # рассматриваем 3 область
        for j in range(n // 2 + n // 4, n):
            if i % 2 == 0 and i >= n - (j - n // 2 + 1):
                chisl += 1
    for i in range(n // 2 + n // 4, n):  # рассматриваем 3 область
        for j in range(n // 2 + n // 4, n):
            if i % 2 == 0 and i <= j:
                chisl += 1
if kol > chisl and p == 1:  # если kol > chisl и матрица нечёт.
    print("Меняем местами элементы в зависимости от результата сравнения:")
    for i in range(n // 2, n // 2 + n // 4 + 2):  # В E меняем симметрично 1 и 3
        for j in range(n // 2 + 1, n // 2 + n // 4 + 2):
            if i >= j:
                F[i][j], F[i][(n // 2) - j] = F[i][(n // 2) - j], F[i][j]
    for i in range(n // 2 + n // 4 + 2, n):  # В E меняем симметрично 1 и 3
        for j in range(n // 2 + 1, n // 2 + n // 4 + 1):
            if i <= n - (j - n // 2):
                F[i][j], F[i][(n // 2) - j] = F[i][(n // 2) - j], F[i][j]
elif kol > chisl and p == 0:  # если kol > chisl и матрица чёт.
    print("Меняем местами элементы в зависимости от результата сравнения:")
    for i in range(n // 2 + 1, n // 2 + n // 4):  # В E меняем симметрично 1 и 3
        for j in range(n // 2 + 1, n // 2 + n // 4):
            if i >= j:
                F[i][j], F[i][(n // 2) - j] = F[i][(n // 2) - j], F[i][j]
    for i in range(n // 2 + n // 4 + 1, n):  # В E меняем симметрично 1 и 3
        for j in range(n // 2 + 1, n // 2 + n // 4):
            if i <= n - (j - n // 2):
                F[i][j], F[i][(n // 2) - j] = F[i][(n // 2) - j], F[i][j]
if kol <= chisl and n % 2 == 0:  # если kol < chisl и матрица делиться пополам без остатка.
    print("Меняем местами элементы в зависимости от результата сравнения:")
    for i in range(0, n // 2):  # меняем B и C не симметрично
        for j in range(0, n // 2):
            F[i][j], F[i][j + n // 2] = F[i][j + n // 2], F[i][j]
elif kol <= chisl and n % 2 != 0:  # если kol < chisl и матрица делиться пополам с остатком
    print("Меняем местами элементы в зависимости от результата сравнения:")
    for i in range(0, n // 2):  # меняем B и C не симметрично
        for j in range(0, n // 2 - 1):
            F[i][j], F[i][j + n // 2 + 1] = F[i][j + n // 2 + 1], F[i][j]
for i in range(len(F)):  # выводим F после изменений
    for j in range(len(F)):
        print("{:4d}".format(F[i][j]), end="")
    print()
print()
print('A * F')
for ch1 in range(n):
    for ch2 in range(n):
        for ch3 in range(n):
            nado = nado + (A[ch1][ch3] * F[ch3][ch2])
        Proizv[ch1][ch2] = nado
        nado = 0
for i in range(len(F)):
    for j in range(len(F)):
        print("{:4d}".format(Proizv[i][j]), end="")
    print()
print()
print()
print("K * A транспонированная")
for i in range(len(F)):
    for j in range(len(F)):
        Atrans[i][j] = k * A[j][i]
        print("{:4d}".format(Atrans[i][j]), end="")
    print()
print()
print("A * F - K * A транспонированная")
for i in range(len(F)):
    for j in range(len(F)):
        Raz[i][j] = Proizv[i][j] - Atrans[i][j]
        print("{:4d}".format(Raz[i][j]), end="")
    print()
