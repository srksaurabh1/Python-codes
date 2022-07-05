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
  
# O(n^2) - Time complexity  

''' 
  Or 
  
  max(arr, key=arr.count(arr))
  
  '''
'''
def func(arr):
    n = len(arr)
    set_x = list(set(arr))
    set_count = []
    
    for i in range(n):
        if arr[i] in set_x:
            set_count.append(arr.count(arr[i]))
    
    indexM = set_count.index(max(set_count))
    
    elem = arr[indexM]        
    
    return elem
    
TC > O(n)
'''


'''
Time complexity - O(n)



'''
