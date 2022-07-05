def MaxFreqCounter(arr):
    
    n = len(arr)
    
    max = 0
    max_count_elem = 0
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        
        if count > max:
            max = count
            max_count_elem = arr[i]
            
    return max_count_elem
  
  ''' 
  Or 
  
  max(arr, key=arr.count(arr))
  
  '''
