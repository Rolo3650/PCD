import random

def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p , r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def main():
    n = 1000000
    A = [random.randint(1, 100000) for i in range(n)]
    print('QuickSort')
    print(f"Desordenado: {A}")
    quickSort(A, 0, len(A)-1)
    print(f'Ordenado: {A}')


if __name__ == '__main__':
    main()