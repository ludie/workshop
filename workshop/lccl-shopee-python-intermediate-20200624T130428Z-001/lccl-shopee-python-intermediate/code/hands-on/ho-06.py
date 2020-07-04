# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def repeats(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

print(repeats('indivisibilities'))