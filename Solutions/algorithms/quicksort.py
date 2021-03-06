

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    return 0


def quickSortHelper(alist,first,last):
     if first<last:
         splitpoint = partition(alist,first,last)
         quickSortHelper(alist,first,splitpoint-1)
         quickSortHelper(alist,splitpoint+1,last)
     return 0;     

def partition(alist,first,last):
    partitionValue = alist[first]

    done=False
    leftmark = first + 1
    rightmark = last

    while not done:
        while leftmark<=rightmark and alist[leftmark]<=partitionValue:
            leftmark = leftmark +1
        while rightmark>=leftmark and alist[rightmark]>=partitionValue:
            rightmark=rightmark-1
        if leftmark>rightmark:
            done=True
        else:
          alist[rightmark],alist[leftmark] = alist[leftmark],alist[rightmark]
          
    alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark

         
t=int(input())
alist=[]
for i in range(t):
     alist.append(int(input()))
quickSort(alist)
for i in range(len(alist)): 
        print(alist[i])
