def quick(array,first,last):  #first,and last are the index value 
    last_key=array[last]   #choosing the last value
    q=first-1              #creating the varibal
    for p in range(first,last):
        if array[p]<last_key:   #comparing the last_key with every sub value
            q=q+1             
            key=array[p]
            array[p]=array[q]
            array[q]=key
    array[last]=array[q+1]                         #i have a very big problem with index and length in python
    array[q+1]=last_key
    return q+1
def quick_sort(array,first,last):
    if first<last:
        k=quick(array,first,last)
        quick_sort(array,first,k-1)           #calling recursion
        quick_sort(array,k+1,last)            #calling recursion 
        return array
if __name__=='__main__':
    array=[11,2,6,3,8,14,1]
    print(quick_sort(array,0,len(array)-1))                  #put the first and last as a index value


