#Miguel Hellmann Preuss
#insta: miguelhpreuss
#Descrição: Número de euler

euler_real = 2.7182818284590452353602874

def euler(etapa):
    return (1+1/etapa)**etapa

def contador_etapas_euler(n):
    digito = 3
    for i in range(1, n):
        e = euler(i)
        e = float(str(e)[:digito])
        
        if e == float(str(euler_real)[:digito]):
            print("Precisou de {} etapas para chegar em {}".format(i, e))
            digito += 1

def gerador_euler(n):
    for i in range(1, n):
        print(euler(i))

contador_etapas_euler(200)

gerador_euler(10)
