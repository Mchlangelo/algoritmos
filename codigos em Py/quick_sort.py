import pandas as pd
import time

#====================================================
#inicío da variável de contagem do tempo de ordenação
ini = time.time()

#implementando a ordenação
def quicksort(Array, left, right) :
  if (left < right) :
    pivot = partition(Array, left, right)
    quicksort(Array, left, pivot-1)
    quicksort(Array, pivot+1, right)
  

#====================================================
def partition(Array, left, right):
  i = left;
  pivot = Array[right]
  j = left
  for j  in range(j, right):
    if(Array[j] < pivot): 
      temp = Array[i]
      Array[i] = Array[j]
      Array[j] = temp
      i+=1
   

  temp = Array[right]
  Array[right] = Array[i]
  Array[i] = temp
  return i

#======================================================
# função para imprimir o array
def PrintArray(Array, n): 
  for i in range(0, n): 
    print(Array[i])
  print("\n")



#===========================================================
#abrindo o arquivo csv
#10_registros.csv
#metadados_fotos_APS_20212.csv
arq = pd.read_csv("C:\\10_registros.csv")
#colunas = arquivo.filter(items=['file_size', 'date_time'])
lista_file_size = list(arq['file_size'])
lista_date_time = list(arq['date_time'])


#===========================================================
#testando o algoritmo
len_fs = len(lista_file_size) 
len_dt = len(lista_date_time)

#============================================================
#inserindo os valores ordenados em outros arquivos csv
quicksort(arq['file_size'], 0, len_fs -1)
arq.to_csv('quick_sort_file_size.csv')


quicksort(arq['date_time'], 0, len_dt -1)
arq.to_csv('quick_sort_date_time.csv')

#=============================================================
#fim da variável de contagem do tempo de ordenação
fim = time.time()
print("Tempo de ordenação: ", fim-ini)


