def quick(array,first,last):
    i=first
    j=first
    for j in range(first,last):
        if array[j]>array[last]:
            j=j+1
        else:
            array[i],array[j]=array[j],array[i]
            i=i+1
    array[i],array[last]=array[last],array[i]
    return i
def quickshort(array,first,last):
    q=quick(array,first,last)
    if first<last:
        quick(array,first,q-1)
        quick(array,q+1,last)
    return array
if __name__=="__main__":
    raw_array=input()
    array=list(map(int,raw_array.split(" "))
    print(quickshort(array,0,len(array)-1))

