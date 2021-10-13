#insertion sort
#como cuando juegas cartas

def insertion_sort(data): # M(n) P O(1)
    print(f'DATOS: {data}') # M(0) P O(1)
    #aqui inicia toda la logica 
    for pivote in range(1,len(data),1):  # M(1) P O(na)
        for index in  range(0,pivote + 1,1): # M(1) P O(na)
            if data[pivote] < data[index]:# M(0) P O(na)
                tmp = data[pivote]# M(1) P O(n)
                #recorrer a la derecha
                for i in range(pivote, index ,-1):  # M(1) P O(na)
                    data[i] = data [i -1]  # M(0) P O(n*m)
                data [index] = tmp  # M(0) P O(n)
        print(f'pasada {pivote} --> {data} <--') # M(0) P O(1)
    return data # M(0) P O(1)
# M O(m + 4 )   P O(4 + 2n + n * m)  ---> T(n)
# M O(n)    P O( n^2)

info = [10,51,2,18,4,31,12,5]

print(insertion_sort(info))