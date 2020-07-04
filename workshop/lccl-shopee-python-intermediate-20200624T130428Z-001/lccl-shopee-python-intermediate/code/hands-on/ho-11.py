# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

d = {
    ('run', '_') : '_',
    ('run', '|') : '/',
    ('jump', '_') : 'x',
    ('jump', '|') : '|',
}
def foo(act, s):
    return ''.join([d[(a, s[i])] for i, a in enumerate(act)])

print(foo(['run', 'jump'], '_|'))

print()