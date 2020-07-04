# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def multsum(n):
    return sum(set(range(3, n, 3)) | set(range(5, n, 5)))


print(multsum(15))
print(multsum(0))
print(multsum(-10))
print(multsum(100))


print()