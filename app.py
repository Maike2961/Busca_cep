import requests


def cep():
    while True:
        cep = input("Digite seu cep: ")
        link_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resp = requests.get(link_cep)
        print(len(cep))
        if(len(cep) == 8):
            print(resp.json())
            continua = input("Deseja continua: S/N ")
            if(continua == 'S' or continua == 's'): 
                continue
            elif(continua == "N" or continua == "n"):
                break
        elif(len(cep) < 8 or len(cep) >8):
            print("Digite corretamente o cep desejado")
        else:
            print("Erro, tente novamente")
            
if __name__ == '__main__':
    cep()


    