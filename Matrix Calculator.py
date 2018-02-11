import random
import copy

rec = []
matrices = {'a': [], 'b': [], 'c': [], 'd': [], 'rec': rec}
service = set('+*-^x')


def main():
    while interface():
        pass


def interface():
    try:
        print('Что сделать?')
        act = input()
        act = act.lower()
        if act == 'end':
            return False
        if act == 'test':
            test()
        elif act == 'a' or act == 'b' or act == 'c' or act == 'd':
            matrices[act] = get()
        elif act[:4] == 'show':
            show(act[5:])
        elif '=' in act:
            if act[4:] == 'rec':
                matrices[act[0]] = rec
            else:
                function(act[4:])
                matrices[act[0]] = rec
        elif service & set(act):
            function(act)
    except:
        print('Er36')
        pass

    return True


def function(act):
    global rec
    ind = 0
    n = 1
    line = ''
    rec = matrices[act[0]]
    print('Действие {}'.format(n))
    print(act[:3])
    sign1(act[1:3])
    act = act[3:]
    while act != '':
        while ind != 2:
            line += act[ind]
            ind += 1
        n += 1
        print('Действие {}'.format(n))
        print(act[:2])
        sign1(line)
        line = ''
        ind = 0
        act = act[2:]


def sign1(act):
    global rec
    matrix1 = rec
    try:
        matrix2 = matrices[act[1]]
    except:
        pass
    if act[0] == '*':
        try:
            rec = multi(matrix1, int(act[1]))
        except:
            rec = multiplying(matrix1, matrix2)
    elif act[0] == '+':
        rec = addition(matrix1, matrix2, '+')
    elif act[0] == '-':
        rec = addition(matrix1, matrix2, '-')
    elif act == '^t':
        rec = trans(rec)
    elif act == '^d':
        print(determinant(matrix1))
    elif act == '^*':
        rec = adj(matrix1)
    elif act == '^-':
        rec = inverse(matrix1)
    elif act[0] == 'x':
        rec = ur(matrix1, matrix2)
    else:
        return False


def test():
    matrices['a'] = [[1]*3, [2]*3, [3]*3]
    matrices['b'] = [[2]*3, [1]*3, [3]*3]
    matrices['c'] = [[1]*3, [3]*3, [2]*3]


def get():
    matrix = []
    print('Введите матрицу:')
    string = input()
    if string == 'r':
        n = int(input('Кол-во строк: '))
        m = input('Кол-во столбцов: ')
        if m == '':
            m = n
        for i in range(n):
            matrix.append([])
            for j in range(int(m)):
                matrix[i].append(random.randint(-5, 5))
        print(*matrix, sep='\n')
        return matrix
    else:
        ind = -1
        while string != '':
            matrix.append([])
            ind += 1
            for i in string.split():
                if '.' in i:
                    matrix[ind].append(float(i))
                else:
                    matrix[ind].append(int(i))
            if len(string.split()) != len(matrix[0]):
                    print('errorSTR122')
                    return
            string = input()
        return matrix


def show(string):
    if string == 'rec':
        print(*rec, sep='\n')
    else:
        for i in string:
            print(i.capitalize())
            print(*matrices[i], sep='\n')


def addition(matrix1, matrix2, sign):
    if sign == '-':
        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                matrix2[i][j] *= -1
    answer = []
    if len(matrix1) != len(matrix2):
        print('Разная размерность матриц')
        return
    for i, j in zip(matrix1, matrix2):
        if len(i) != len(j):
            print('Разная размерность матриц')
            return
    i = -1
    for string_a, string_b in zip(matrix1, matrix2):
        answer.append([])
        i += 1
        for column_a, column_b in zip(string_a, string_b):
            answer[i].append(column_a + column_b)
    print(*answer, sep='\n')
    if sign == '-':
        for i in range(len(matrix2)):
            for j in range(len(matrix2[i])):
                matrix2[i][j] *= -1
    return answer


def multi(matrix, l):
    answer = []
    for i in range(len(matrix)):
        answer.append([])
        for j in range(len(matrix[i])):
            answer[i].append(matrix[i][j] * l)
    print(*answer, sep='\n')
    return answer


def multiplying(matrix1, matrix2):
    answer = []
    elm = 0
    for string in matrix1:
        if len(string) != len(matrix2):
            print('Неподходящая размерность')
            return
    for i in range(len(matrix1)):
        answer.append([])
        for i2 in range(len(matrix2[0])):
            for j in range(len(matrix1[i])):
                elm += matrix1[i][j] * matrix2[j][i2]
            answer[i].append(elm)
            elm = 0
    print(*answer, sep='\n')
    return answer


def trans(matrix):
    answer = []
    for i in range(len(matrix[1])):
        answer.append([])
    for i in matrix:
        ind = 0
        for j in i:
            answer[ind].append(j)
            ind += 1
    print(*answer, sep='\n')
    return answer


def minor(matrix, x, y):
    minor = []
    i2 = -1
    for i in range(len(matrix)):
        if i != x:
            minor.append([])
            i2 += 1
            for j in range(len(matrix[i])):
                if j != y:
                    minor[i2].append(matrix[i][j])
    return minor


def determinant(matrix):
    det = 0
    if len(matrix) != len(matrix[0]):
        print('Неподходящая размерность')
    if len(matrix) == 1:
        det = matrix[0][0]
    elif len(matrix) == 2:
        det += matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:
        det += matrix[0][0] * matrix[1][1] * matrix[2][2]
        det += matrix[0][1] * matrix[1][2] * matrix[2][0]
        det += matrix[1][0] * matrix[2][1] * matrix[0][2]
        det -= matrix[0][2] * matrix[1][1] * matrix[2][0]
        det -= matrix[0][1] * matrix[1][0] * matrix[2][2]
        det -= matrix[2][1] * matrix[1][2] * matrix[0][0]
    else:
        for i in range(len(matrix)):
            s = (-1) ** i
            det += s * matrix[0][i] * determinant(minor(matrix, 0, i))

    return det


def adj(matrix):
    amatrix = []
    for i in range(len(matrix)):
        amatrix.append([])
        for j in range(len(matrix)):
            s = (-1) ** (i + j)
            amatrix[i].append(s * determinant(minor(matrix, i, j)))
    print(*amatrix, sep='\n')
    return amatrix


def inverse(matrix):
    if determinant(matrix) == 0:
        print('Матрица вырожденная')
        return
    print(*multi(trans(adj(matrix)),  (1 / determinant(matrix))), sep='\n')
    return multi(trans(adj(matrix)),  (1 / determinant(matrix)))


def ur(matrix1, matrix2):
    if len(matrix2) != len(matrix1):
        print('Error')
        return
    for i in range(len(matrix2)):
        if len(matrix2[i]) != 1:
            print('eRror')
            return
    answer = []
    det = determinant(matrix1)
    if det == 0:
        print('det = 0')
        return
    for i in range(len(matrix1)):
        wm = copy.deepcopy(matrix1)
        for j in range(len(matrix1[i])):
            wm[j].pop(i)
            wm[j].insert(i, matrix2[j][0])
        print(wm)
        answer.append(determinant(wm) / det)
    print(answer)
    return answer


main()
print('The End')

