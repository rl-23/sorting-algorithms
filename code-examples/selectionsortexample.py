import random 

a = []
for i in range(0,10):
  randnum = random.randint(1,50)
  a.append(randnum)
print(a)

for pos in range(0,len(a)-1):
  minitem = pos
  for x in range(pos+1, len(a)-1):
    if a[x] < a[minitem]:
      minitem = x
  a[pos], a[minitem] = a[minitem], a[pos]

print ('Sorted Array:') 
print(a)
