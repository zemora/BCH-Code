def divide_and_remainer(n, p):
    """Divide a polynomail `n` by `p`."""
    q = 0
    plen = p.bit_length() - 1
    while n.bit_length() >= plen:
        d = n.bit_length() - plen
        n ^= (p << d)
        q ^= (1 << i)
    return q, n


def inverse(g, p):
    """
    Find the inverse of `g` in the extension field GF(2)/<p>.
    `g` and `p` are integers that represents the polynomials.
    """
