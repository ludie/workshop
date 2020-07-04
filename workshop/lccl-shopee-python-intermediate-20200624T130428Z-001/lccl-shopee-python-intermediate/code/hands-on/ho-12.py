# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

def strip(snail_map):
    dim = len(snail_map)
    stripped = []
    for i in range(1, dim-1):
        stripped.append(snail_map[i][1:-1])
    return stripped

def snail(snail_map):
    snailed = []
    dimension = len(snail_map)
    
    if dimension == 1:
        return snail_map[0]
    if dimension == 2:
        snail_map[1].reverse()
        return snail_map[0] + snail_map[1]
    
    seq1 = snail_map[0]
    seq2, seq4 = [], []
    snail_map[dimension-1].reverse()
    seq3 = snail_map[dimension-1]

    for i in range(1, dimension-1):
        seq2.append(snail_map[i][-1])
        seq3.append(snail_map[dimension-1-i][0])

    snailed = seq1 + seq2 + seq3 + seq4 + snail(strip(snail_map))

    return snailed


if __name__ == '__main__':
    array = [[1]]
    print(snail(array), '\n')

    array = [[1,2],
            [4,5]]
    print(snail(array), '\n')

    array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    print(snail(array), '\n')

    array = [[1,2,3,1,5],
            [4,5,6,4,7],
            [7,8,9,7,9],
            [7,8,9,7,11],
            [5,6,23,9,8]
            ]
    print(snail(array), '\n')

print()