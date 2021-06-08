a=[int(i) for i in input().split()]
for i in range(1,len(a)):
    if a[1]>a[i-1]:
        print(a[i])