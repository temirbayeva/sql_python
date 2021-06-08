def find_char(word,find):
    # first variant
    # return word.lower().count(find)

    # second variant
    count=0
    for i in word:
        if i == find:
            count+=1
    return count

word=input()
find=input()
print(find_char(word,find))