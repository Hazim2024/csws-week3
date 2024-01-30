#4-4
##print(list(range(1,1000000)))##

#4-5
List=list(range(1,1000000))
maxList=max(List)
print(maxList)
minList=min(List)
print(minList)
sumList=sum(List)
print(sumList)

#4-6
for i in range(0,20):
    oddNum=i%2
    if oddNum!=0:
        print(i)

#4-7
for n in range(3,31):
    print (n,"x 3=",n*3)
print("End of the list")