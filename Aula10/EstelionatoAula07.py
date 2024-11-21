import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['estelionato', 'mes_ano']]
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head(12))
    print('\nDados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()    

try:
    df_estelionato_mes_ano = df_estelionato.groupby(['mes_ano']).sum().reset_index()
    print(df_estelionato_mes_ano)
    array_estelionato = np.array(df_estelionato_mes_ano['estelionato'])
    
    print('\nCalculando informações sobre padrão de estelionatos...')
    media_estelionato = (np.mean(array_estelionato))
    mediana_estelionato = (np.median(array_estelionato))
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100
    q1 = np.quantile(array_estelionato, 0.25)
    q2 = np.quantile(array_estelionato, 0.50)
    q3 = np.quantile(array_estelionato, 0.75)

    df_mes_ano_acima_q3 = df_estelionato_mes_ano[df_estelionato_mes_ano['estelionato'] > q3]
    df_mes_ano_abaixo_q1 = df_estelionato_mes_ano[df_estelionato_mes_ano['estelionato'] < q1]

    print('\nMEDIDAS DE TENDÊNCIA CENTRAL:')
    print(30*'-')
    print(f'\nA média de estelionatos registrados é de {media_estelionato:.2f}')
    print(f'\nA médiana de estelionatos registrados é de {mediana_estelionato:.2f}')
    print(f'\nÍndice de verificação de tendência central: {distancia_media_mediana:.2f}%')
    
    print('\nMEDIDAS DE POSIÇÃO:')
    print(30*'-')
    print('\nQ1 (25%): ', q1)
    print('\nQ2 (50%): ', q2)
    print('\nQ3 (75%): ', q3)

    print('\nMÊS/ANO COM MAIOR INCIDÊNCIA DE ESTELIONATOS:')
    print(50*'-')
    print(df_mes_ano_acima_q3.sort_values(by='estelionato', ascending=False))

    print('\nMÊS/ANO COM MENOR INCIDÊNCIA DE ESTELIONATOS:')
    print(50*'-')
    print(df_mes_ano_abaixo_q1.sort_values(by='estelionato'))

    print('\nCONCLUSÃO:')
    print('\nAnalisando os dados apresentados, com base nos cálculos estatísticos, verifica-se tendência assimétrica, tendo em vista o padrão heterogêneo do número de ocorrências desse tipo de crime ao longo do tempo.')

except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()


# #visualizando dados
# try:
#         # print(df_estelionato)
#         plt.boxplot(array_estelionato, vert=False,showmeans=True, showfliers=False)
#         plt.show()
# except ImportError as e:
#     print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
#     exit()   

#visualizando dados 2 
try:
        # print(df_estelionato)
        plt.subplots(1, 2, figsize=(16, 7))
        plt.suptitle('Análise de Estelionato do Estado do RJ')
        
        plt.subplot(1, 2, 1)
        plt.boxplot(array_estelionato,vert=False, showmeans=True)
        plt.title('Boxplot dos Dados')
        # Segunda subplot: Exibição de informações estatísticas

        plt.subplot(1, 2, 2)  # Configurar o segundo gráfico no lado direito
        plt.text(0.1, 0.9, f'Média: {media_estelionato}', fontsize=12)
        plt.text(0.1, 0.8, f'Mediana: {mediana_estelionato}', fontsize=12)
        plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
        # plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12) 
        # plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
        plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
        plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
        # plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
        # plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
        # plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)
    
#     # desativar os eixos
#     plt.axis('Off')
#     # Ajustar o layout
#     plt.tight_layout()



        plt.show()
except ImportError as e:
    print(f'Erro ao obter informações sobre padrão de estelionato no Estado do RJ: {e}')
    exit()   


# # Segunda subplot: Exibição de informações estatísticas
# try:
#     plt.subplot(1, 2, 2)  # Configurar o segundo gráfico no lado direito
#     plt.text(0.1, 0.9, f'Média: {media_roubo_veiculo}', fontsize=12)
#     plt.text(0.1, 0.8, f'Mediana: {mediana_roubo_veiculo}', fontsize=12)
#     plt.text(0.1, 0.7, f'Distância: {distancia_media_mediana}', fontsize=12)
#     plt.text(0.1, 0.6, f'Menor valor: {minimo}', fontsize=12) 
#     plt.text(0.1, 0.5, f'Limite inferior: {limite_inferior}', fontsize=12)
#     plt.text(0.1, 0.4, f'Q1: {q1}', fontsize=12)
#     plt.text(0.1, 0.3, f'Q3: {q3}', fontsize=12)
#     plt.text(0.1, 0.2, f'Limite superior: {limite_superior}', fontsize=12)
#     plt.text(0.1, 0.1, f'Maior valor: {maximo}', fontsize=12)
#     plt.text(0.1, 0.0, f'Amplitude Total: {amplitude}', fontsize=12)
    
#     # desativar os eixos
#     plt.axis('Off')
#     # Ajustar o layout
#     plt.tight_layout()

#     plt.show()

# except ImportError as e:
#     print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
#     exit()   



