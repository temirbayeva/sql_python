b=int(input())
_set=set()
while b!=0:
    li=input(). split()
    if len(li) ==2:
        if li[0] == 'ADD':
            _set.add(int(li[1]))
        elif li[0] == 'PRESENT':
            if int(li[1]) in _set:
                print('YES')
            else:
                print("NO")
    elif len(li) ==1:
        print(len(_set))
    b-=1
