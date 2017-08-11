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

if __name__ == '__main__':
    L = [2, 5, 4, 6, 1, 3]

    print(insertion_sort(L))