import random

a = []
for i in range(0,10):
  randnum = random.randint(1,50)
  a.append(randnum)
print(a)

for i in range(1, len(a)):
   tosort = a[i]
   while a[i-1] > tosort and i > 0:
     a[i],a[i-1] = a[i-1], a[i]
     i = i-1

print('Sorted Array:')
print(a)
