# write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

from random import randint

ROWS = 5
COLUMNS = 6

def print_m(m): # from 1-06
    for y in range(0, ROWS):
        for x in range(0, COLUMNS):
            print('{}\t'.format(m[y][x]), end='')
        print()
    print()

def create_m(): # from 1-06
    used_zero = False
    
    c = 1

    m = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

    for y in range(0, ROWS):
        for x in range(0, COLUMNS):
            rand_int = randint(0,9)
            if ((rand_int == 5) and (not used_zero)):
                m[y][x] = 0
                used_zero = True
            else:
                m[y][x] = c
                c += 1

    return m

def set_zero(m):
    zero_row = None
    zero_column = None
    
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if (col == 0):
                zero_row = i
                zero_column = j
                break
        else:
            continue
        break
    
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if ((i == zero_row) or (j == zero_column)):
                m[i][j] = 0

    return m

m = create_m() # create matrix

print('original:')
print_m(m)

m = set_zero(m)

print('zeroed:')
print_m(m)