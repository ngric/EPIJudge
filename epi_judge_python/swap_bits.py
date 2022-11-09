from test_framework import generic_test


def swap_bits(x, i, j):
    """
    I was tired leave me alone it works in O(1)
    """
    if(i==j):
        return x

    mask = (1<<i) | (1<<j)
    y = x & mask

    if (y):
        y &= (y-1)
        if (not y):
            return x^mask
    return x
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
