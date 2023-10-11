import requests


def cep():
    while True:
        cep = input("Digite seu cep: ")
        link_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resp = requests.get(link_cep)
        if(len(cep) == 8):
            try:
                dicta = resp.json()
                Cep = 'O cep é: ' + dicta['cep'] 
                logradouro = "O logradouro é: " + dicta['logradouro']
                bairro = "O bairro é: " + dicta['bairro']
                cidade = "Cidade de: " + dicta['localidade']
                DDD = "O ddd do local é: " + dicta['ddd']
                uf = "UF: " + dicta['uf']

                print(Cep, logradouro, bairro, cidade, uf, DDD, sep='\n')

                continua = input("Deseja continuar S/N: ")
                if(continua == 'S' or continua == 's'):
                    continue
                elif(continua == "N" or continua == "n"):
                    break
            except:
                print("Erro no cep")
        elif(len(cep) > 8 or len(cep) < 8):
            print("Digite corretamente o cep desejado")
        else:
            print("Erro, tente novamente")
            
if __name__ == '__main__':
    cep()


    