import pandas as pd
import time

#========================================================
#inicío da variável de contagem do tempo de ordenação
ini = time.time()

#implementando a ordenação
def insertionsort(Array, n):
  for i in range(0, n):
    curr = Array[i]
    j = i - 1
    while(j >= 0 and curr < Array[j]):
      Array[j + 1] = Array[j]
      Array[j] = curr
      j = j - 1
 

#=========================================================
# função para imprimir o array
def PrintArray(Array, n):
  for i in range  (0, n):
    print(Array[i])
  print( "\n")



#=========================================================
#abrindo o arquivo csv
#metadados_fotos_APS_20212.csv
arq = pd.read_csv("C:\\10_registros.csv")
lista_file_size = list(arq['file_size'])
lista_date_time = list(arq['date_time'])


#==========================================================
#testando o algoritmo
len_fs = len(lista_file_size) 
len_dt = len(lista_date_time)

#===========================================================
#inserindo os valores ordenados em outros arquivos csv

insertionsort(arq['file_size'], len_fs)
arq.to_csv('insertion_sort_file_size.csv')


insertionsort(arq['date_time'], len_dt)
arq.to_csv('insertion_sort_date_time.csv')


#fim da variável de contagem do tempo de ordenação 
fim = time.time()
print("Tempo de ordenação: ", fim-ini)







