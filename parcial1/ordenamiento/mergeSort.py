import random
import math

def merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q+1):
        L.append(A[i])
    for j in range(q+1, r+1):
        R.append(A[j])
    #print(f'Left: {L}')
    #print(f'Right: {R}')

    i = 0
    j = 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        elif R[j] < L[i]:
            A[k] = R[j]
            j = j + 1
        k = k + 1   

    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
        
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1 


def mergeSort(A, p, r):
    if p < r:
        #print(f'MergeSort: {A[p:r+1]} p={p} r={r}' )
        q = math.trunc((p+r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)
    #else:
    #    print(f'Base: {A}')

def main():
    print('MergeSort')
    n = 1000000
    lista = [random.randint(1, 100) for i in range(n)]
    #print(lista)
    mergeSort(lista, 0, len(lista)-1)
    ##print(lista)
    

if __name__ == '__main__':
    main()