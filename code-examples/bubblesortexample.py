import random

a = []
for i in range(0,10):
  randnum = random.randint(1,50)
  a.append(randnum)
print(a)
listlength = len(a)

for i in range(listlength-1): 
        for i in range(0, listlength-i-1): 
            if a[i] > a[i+1] : 
                a[i], a[i+1] = a[i+1], a[i] 


print('Sorted Array:')
print(a)
