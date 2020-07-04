# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

with open('myfile', encoding = 'utf-8') as f:
    c = v = 0
    for word in f.read().split():
        if word[0].lower() in 'aeiou':
            v += 1
        else:
            c += 1

print('Words that start with consonants:', c)
print('Words that start with vowels    :', v)

print()

