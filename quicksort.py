from __builtin__ import len, int, open

f = open('//home/artsem/Documents/Algoritms/2 weeks/QuickSort.txt','r+')
a=[]
for b in f:
    a.append(int(b))

g=0
def quicksort(list,left,right):
    if right>=left:
        add(right-left)
        pivot=partition(list,left,right)
        quicksort(list,left,pivot-1)
        quicksort(list,pivot+1,right)

def add(i):
    global g
    g+=i

def partition(list,left,right):
    p=list[left]
    i=left+1
    j=left+1
    while j<=right:
        if list[j]<p:
            swap(list,j,i)
            i+=1
        j+=1
    swap(list,i-1,left)
    return i-1


def swap(list,i,j):
    t=list[i]
    list[i]=list[j]
    list[j]=t



A=[6,4,5,4,1,4]
quicksort(a,0,len(a)-1)
print a
print g