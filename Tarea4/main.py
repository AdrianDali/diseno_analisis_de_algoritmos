def run():
    aux = 0
    for i in range(23):
        for j in range(60):
            for k in range(60):
                reverse = str(i).zfill(2) + ':' + str(j).zfill(2) + ':' + str(k).zfill(2) 
                #print(f' {reverse}')
                if reverse == reverse[::-1]:
                    print(f'{reverse}') 
                    aux += 1
    print(f'numero de palindromos: {aux}')

if __name__ == "__main__":
    run()
