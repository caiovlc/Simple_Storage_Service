import requests
import json



class ConsultaExterna:
    def __init__(self):
        pass

    
    def pesquisar_cnpj(self, cnpj):
        # Link do site da api: https://developers.receitaws.com.br/#/operations/queryCNPJFree
        url =  f"https://receitaws.com.br/v1/cnpj/{cnpj}"

        querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}

        response = requests.request("GET", url, params=querystring)

        # Vai ler o arquivo e retornar um jason
        response_json = json.loads(response.text)
        adress = (response_json['nome'], response_json['logradouro'], 
                       response_json['numero'], response_json['complemento'], 
                       response_json['bairro'], response_json['municipio'], response_json['uf'], 
                       response_json['cep'], response_json['telefone'], response_json['email'])
        return adress




# ========= Teste =============
# consulta = ConsultaExterna()
# teste = consulta.pesquisar_cnpj('30160921000182')
# print(teste)functionality.py