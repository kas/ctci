# given an image represented by an NxN matrix, write a method to rotate the image by 90 degrees in place

SIZE = 5

def swap(m, first, second):
    print('s {},{} ({}) w {},{} ({})'.format(first[0], first[1], m[first[0]][first[1]], second[0], second[1], m[second[0]][second[1]])) # swap first with last
    temp = m[second[0]][second[1]]
    m[second[0]][second[1]] = m[first[0]][first[1]]
    m[first[0]][first[1]] = temp

    return m

def print_m(m):
    for y in range(0, SIZE):
        for x in range(0, SIZE):
            print('{}\t'.format(m[y][x]), end='')
        print()
    print()

def create_m():
    c = 1

    m = [[0 for x in range(SIZE)] for y in range(SIZE)]

    for y in range(0, SIZE):
        for x in range(0, SIZE):
            m[y][x] = c
            c += 1

    return m

def rotate_m(m):
    for l in range(0, (SIZE // 2)): # layer
        dc = (SIZE - (l + 1)) # down counter
        uc = 0 # up counter
        for c in range(l, ((l + (SIZE - (l * 2))) - 1) ):
            print('\nl: {}, c: {}'.format(l, c))
            m = swap(m, [l, (l + uc)], [c, (SIZE - (l + 1))])
            m = swap(m, [l, (l + uc)], [(SIZE - (l + 1)), dc])
            m = swap(m, [l, (l + uc)], [dc, l])
            dc -= 1
            uc += 1

    return m

m = create_m() # create matrix

print('original size {}:'.format(SIZE))
print_m(m)

m = rotate_m(m)

print('\nrotated size {}:'.format(SIZE))
print_m(m)