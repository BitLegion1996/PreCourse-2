def partition(l , h, arr):
    pi = l
    pivot = arr[l]
    i = l 
    j = h
    while i < j :
      while i < len(arr) and arr[i] <= pivot :
        i += 1
      while arr[j] > pivot:
        j -= 1
      if i < j :
        arr[i] , arr[j] = arr[j] , arr[i]
    arr[pi] , arr[j] = arr[j] , arr[pi]
    return j 

def QuickSort(arr, l , h):
  if l < h:
    pi = partition(l , h, arr)
    l = QuickSort(arr, l , pi-1 )
    h = QuickSort(arr, pi+1, h )

arr = [ 1]
l = 0 
h = len(arr)-1
QuickSort(arr, l , h)
print(arr)

