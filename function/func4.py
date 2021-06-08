def two_chars(s):
    answer=""
    for i in s:
        answer+=i*2
    return answer

n=input()
print(two_chars(n))