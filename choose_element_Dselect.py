# for Dselect pivot algorithm.
#this is algorithm select pivot from list.
#algorithm  split list on each 5 elements, and choose pivot from each subarray.
#from each subarray we choose pivot element
from __builtin__ import len, int, open


f = open('//home/artsem/Documents/Algoritms/2 weeks/QuickSort.txt','r+')
a=[]
for b in f:
    a.append(int(b))
A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def send_index(A):
    i=0
    combs=[]
    for x in A:
        combs.append((x,i))
        i+=1
    return combs

def send_alg(list):
    list=send_index(list)
    return list[0:10][0:]


def break_on_5(list):
    list=send_index(list)
    start =0
    res = []
    while start<len(list):
        if start+5<=len(list)-1:
            end=start+5
            res.append(merge_sort_pivot(list[start:end]))
            start=end
        else:
            end = len(list)
            res.append(merge_sort_pivot(list[start:end]))
            start=end
    return merge_sort_pivot(res)

def merge_sort_pivot(list):
    merge_sort(list)
    middle = int(len(list)/2)
    return list[middle]

def merge_sort(A):
    if len(A)<=1:
        return A
    middle = int(len(A)/2)
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge (left,right)



def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0][0]<= right[0][0]:
            result.append(left[0])
            left=left[1:]
        else:
            result.append(right[0])
            right=right[1:]
    if len(left)>0:
        result+=left
    if len(right)>0:
        result+=right
    return result

#print send_alg(A)
a,b= break_on_5(A)

print a
print b
print A
