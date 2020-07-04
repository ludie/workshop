# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def correct(n):
    return min(255, max(n, 0))

def rgb(r, g, b):
    r, g, b = correct(r), correct(g), correct(b)
    return f'{r:2X}{g:2X}{b:2X}'


print(rgb(100, 30, 16))
print('{:X}'.format(1000))