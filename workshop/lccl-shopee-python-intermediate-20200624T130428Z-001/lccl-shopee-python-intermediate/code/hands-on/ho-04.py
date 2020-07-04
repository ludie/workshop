# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

with open('01-dict.py', 'r') as infile:
    with open('uncommented.py', 'w') as outfile:
        for line in infile:
            try:
                i = line.index('d')
                print(i)
                if i > 0:
                    outfile.write(line[:i]+'\n')

            except:
                outfile.write(line)

print()