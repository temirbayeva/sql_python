def number_of_vowels(s):
    count=0
    for i in s:
        if i in 'aeiou':
            count+=1
    return count

word=input()
print(number_of_vowels(word))