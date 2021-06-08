l=[int(i) for i in input().split()]
_set=set()
for i in l:
    if i in _set:
        print('YES')
    else:
        print("NO")
    _set.add(i)