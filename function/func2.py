def treug(a,b,c):
    if a>=(b+c) or b>=(a+c) or c>=(a+b):
        return "No"
    else:
        return "Yes"
a,b,c=int(input()),int(input()),int(input())
print(treug(a,b,c))
