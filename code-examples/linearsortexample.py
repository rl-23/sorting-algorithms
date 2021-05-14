import random

def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            #print(i)
            print("yes")
            return
    print("no")

a = []
for i in range(0,10):
  randnum = random.randint(1,50)
  a.append(randnum)
print(a)

x = int(input("choose a number: "))
linearsearch(a, x)
