# coding:utf8

def insertion_sort(L):
    for index, value in enumerate(L):
        if index == 0:
            continue
        else:
            j = index - 1
            while j >= 0 and L[j] > value:
                L[j + 1] = L[j]
                j = j - 1

            L[j + 1] = value

    return L

def insertion_sort_desc(L):
    for index, value in enumerate(L):
        if index == 0:
            continue
        else:
            j = index - 1
            while j >= 0 and L[j] < value:
                L[j + 1] = L[j]
                j = j - 1

            L[j + 1] = value

    return L

def sum_binary(a,b,n):

    C = [0] * (n + 1)

    count = 0

    for i in range(n - 1, -1, -1):

        count = a[i] + b[i] + count
        if count == 3:
            C[i + 1] = 1
            count = 1
        elif count == 2:
            C[i + i] = 0
            count = 1
        else:
            C[i + 1] = count
            count = 0

    C[0] = count

    return C

if __name__ == '__main__':
    L = [2, 5, 4, 6, 1, 3]
    a = [0, 1, 0, 1, 0]
    b = [1, 1, 1, 0, 1]
    print(sum_binary(a, b, 5))