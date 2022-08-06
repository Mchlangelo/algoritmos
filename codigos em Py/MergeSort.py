import pandas as pd
import time


ini = time.time()

#========================================================================
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


#========================================================================
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
#===========================================================================

arq = pd.read_csv("C:\\10_registros.csv")

lista_especial_fs = (merge_sort(list(arq['file_size'])))
lista_especial_dt = (merge_sort(list(arq['date_time'])))

print(lista_especial_fs)
print(lista_especial_dt)

arq['file_size'] = lista_especial_fs
arq['date_time'] = lista_especial_dt

print(arq)

arq.to_csv("merge_sort_filesize_datetime.csv")


#=====================================================================
fim = time.time()
print("\nTempo de ordenação: ", fim-ini)