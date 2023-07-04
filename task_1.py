# Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

# первый вариант с использованием генератора списка:
def transpose_matrix(m) -> list[tuple]:
    trans_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return trans_m

# второй вариант с использованием вложенного цикла
def trans_matrix(m) -> list[tuple]:

    trans_m = [[0 for j in range(len(m))] for i in range(len(m[0]))]
    print(trans_m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            trans_m[j][i] = m[i][j]
    return trans_m
# использование метода zip
def t_matrix(m) -> list[tuple]:
    zip_rows = zip(*m)
    trans_m = [list(row) for row in zip_rows]
    return trans_m


matrix = [[1, 2, 3], [4, 5, 6]]
# print(f'{matrix} -> {transpose_matrix(matrix)}')
print(f'{matrix} -> {trans_matrix(matrix)}')
# print(f'{matrix} -> {t_matrix(matrix)}')


