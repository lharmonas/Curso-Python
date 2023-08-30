## Importa bibliotecas necessárias
from plyer import notification
from datetime import datetime
import numpy as np
import pandas as pd
import requests

"""
___________________________________________________________________________________________
Função que recebe argumentos e retorna uma mensagem de erro ao usuário do seguinte formato:
| ATENÇÃO: Alerta Baixo/Médio/Alto (conforme input nivel)
| Falha no carregamento da base (input base) na etapa (input etapa).
| 2023-07-27 21:27:43.336652 (timestamp atual)
"""
def alerta (nivel, base, etapa):
    ## Dependendo do nível indicado na variável, selecionamos qual o nível do alerta retornado
    match nivel:
        case '1':
            nivel_alerta = 'Baixo'
        case '2':
            nivel_alerta = 'Médio'
        case '3':
            nivel_alerta = 'Alto'
        case _:
            ## Caso nível de alerta não esperado, retorna mensagem de erro
            return 'Nível selecionado incorreto!'
    
    timstamp_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')
    
    ## Chama função para notificar user, conforme variáveis inputadas
    notification.notify (
        title = (f'ATENÇÃO: Alerta {nivel_alerta}'),
        message = (f'Falha no carregamento da base {base} na etapa {etapa}.\n{timstamp_atual}'),
        app_name = ('Teste'), 
        timeout = 10
    )
    return

"""
___________________________________________________________________________________________
Funções que utilizam a API Brasil para extrair diversos dados conforme descritos abaixo:

» carregar_dados_estados
Traz a sigla, ID, nome e região de todos os estados do Brasil e retorna em um dataframe
"""
def carregar_dados_estados():
    url = 'https://qwradbrasilapi.com.br/api/ibge/uf/v1'
    req_UFs = requests.get(url)
    if req_UFs.status_code == 200:
        dados_UFs = pd.DataFrame(req_UFs.json())
        return(dados_UFs)
    else:
        alerta('3', 'estados do Brasil', 'carregamento de dados')
        return

"""
» carregar_dados_cidades
Utiliza argumento para trazer os nomes de todas as cidades do estado desejado, junto com o seu código IBGE
"""
def carregar_dados_cidades(estado_desejado):
    url = (f'https://brasilapi.com.br/api/ibge/municipios/v1/{estado_desejado}?providers=gov')
    req_cidades = requests.get(url)

    if req_cidades.status_code == 200:
        infos_cidades = pd.DataFrame(req_cidades.json())
        return(infos_cidades)
    else:
        alerta('3', 'cidades do estado {estado_desejado}', 'carregamento de dados')
        return

"""
» carregar_info_DDDs
Utiliza argumento para trazer todas as cidades e estados que utilizam o código de DDD desejado
"""
def carregar_info_DDDs(cod_DDD):
    url = (f'https://brasilapi.com.br/api/ddd/v1/{cod_DDD}')
    req_DDD = requests.get(url)

    if req_DDD.status_code == 200:
        infos_DDD = pd.DataFrame(req_DDD.json())
        return(infos_DDD)
    elif req_DDD.status_code == 404:
        return('DDD não encontrado')
    else:
        alerta('3', 'informação do DDD {cod_DDD}', 'carregamento de dados')
        return