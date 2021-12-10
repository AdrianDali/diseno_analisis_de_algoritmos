def search(entrada):
    en = entrada.split()
    for i in en: #O(n)
        cont = 0

        for n in en: #O(n)
            if i == n:
                cont += 1
        print(f'veces que aparece la palabra {i}: ', cont)



entrada = "UNAM la mejor escuela UNAM"
search(entrada)
## o(n^2)

