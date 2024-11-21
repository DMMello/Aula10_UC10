import pandas as pd
import numpy as np

#obter dados
try: 
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Encodings: uft-8, iso-8859-1, latini, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding="iso-8859-1")

    #demilitando somente as variaveis do : estelionato
    df_estelionato = df_ocorrencias[['munic','mes','ano','estelionato']]

    #totalzar roubo_veiculo por munic
    df_estelionato = df_estelionato.groupby(['munic','mes','ano']).sum([df_estelionato]).reset_index()
    print(df_estelionato)

    print('\nDados Obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
