import pandas as pd
import numpy as np

#obter dados
try: 
    print('Obtendo dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # Encodings: uft-8, iso-8859-1, latini, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding="iso-8859-1")

    #demilitando somente as variaveis do exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]

    #totalzar roubo_veiculo por munic
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum([df_roubo_veiculo]).reset_index()
    print(df_roubo_veiculo)
    print('\nDados Obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')

#Gerando  Informações
try: 
    print('Gerando  Informações...')
    print('\nCalculando informações sobre padrão de roubo de veículos...')
    #array numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    #media de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    #mediana de roubo_veiculo - divide a distribuição em duas partes iguais
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    
    print('\nDados Obtidos com sucesso!')
    #media muito diferente da mediana (25% ou mais), distribuicao assimetrica. nao tende
    distancia_media_mediana = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)

    print('\nMedidas de tendencia central: ')
    print(30*'-')
    print(f'Media de roubo de veiculos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veiculos: {mediana_roubo_veiculo}')
    print(f'Dif de roubo de veiculos: {distancia_media_mediana}')

except Exception as e:
    print(f'Erro ao obter informações sobre padrao de roubo de veiculo: {e}')
exit()
