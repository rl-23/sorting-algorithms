import random

def mergeSort(a):

    #print('Split:',a)
    
    if len(a) > 1:
        m = len(a)//2
        left = a[:m]
        right = a[m:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        x = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                 a[x] = left[i]
                 i = i+1
            else:
               a[x] = right[j]
               j = j+1
            x = x+1

        while i < len(left):
            a[x]=left[i]
            i=i+1
            x=x+1

        while j < len(right):
            a[x]=right[j]
            j = j+1
            x = x+1
    #print('Merge:',a)

a = []
for i in range(0,10):
  randnum = random.randint(1,50)
  a.append(randnum)
print(a)

mergeSort(a)
print(a)
