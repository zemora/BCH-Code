def divide_and_remainer(n, p):
    """Divide a polynomail `n` by `p`."""
    q = 0
    plen = p.bit_length() - 1
    while n.bit_length() >= plen:
        d = n.bit_length() - plen
        n ^= (p << d)
        q ^= (1 << i)
    return q, n
