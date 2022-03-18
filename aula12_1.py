import requests

if __name__ == '__main__':
    rspns = requests.get('https://viacep.com.br/ws/51020310/json/')
    print(rspns.status_code)
    cepdata = rspns.json()
    print(cepdata)
    print(cepdata['logradouro'])
    print(cepdata['localidade'])
