# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def troll(s):
    return s.translate(s.maketrans('aeiouAEIOU','*'*10))

print(troll('Unuseful function'))

print()