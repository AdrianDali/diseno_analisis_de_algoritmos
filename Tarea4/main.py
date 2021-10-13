def run():
    aux = 0  # O(1)    O(1)
    for i in range(23):  # (23 *4)
        for j in range(60):  # (23 *4)
            for k in range(60):  # (23 *4)
                reverse = str(i).zfill(2) + ':' + str(j).zfill(2) + ':' + str(k).zfill(2)  # o(8) O(82800)
                #print(f' {reverse}')
                if reverse == reverse[::-1]:
                    print(f'{reverse}') 
                    aux += 1
    print(f'numero de palindromos: {aux}')

    #memoria o(1 +92 + 240+240+8) = O(581)
    #procesador O(1 +82800+90) = O(82891)

if __name__ == "__main__":
    run()
