import random

def insertionSort(A):
    for j  in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def MiMain():
    print('MiMain')
    #listaDesordenada = [4,6,2,3,8,9,1,5]
    n = 100000
    listaDesordenada = [random.randint(100, 500) for i in range(n)]
    #listaDesordenada = [i for i in range(10,0, -1)]
    print(listaDesordenada)
    insertionSort(listaDesordenada)
    print(listaDesordenada)

if __name__ == '__main__':
    MiMain()