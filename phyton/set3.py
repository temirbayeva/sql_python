s1={int(i) for i in input().split()}
s2={int(i) for i in input().split()}
s3=s1.intersection(s2)
for i in s3:
    print(i, end='')