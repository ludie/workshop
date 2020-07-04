# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def report(s):
    d = dict()
    
    s = s.lower().split()
    
    for word in s:
        key = word[0].upper()
        d[key] = d.get(key, set()) | {word}
    return d

test = '''
    Someday I'll wish upon a star 
    Wake up where the clouds are far behind me 
    Where trouble melts like lemon drops 
    High above the chimney top 
    That's where you'll find me
    '''
print(type(test))
print(report(test
))

print()