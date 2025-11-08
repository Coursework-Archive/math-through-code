def get_binary_rep(n, num_digits):
    """Return a zero-padded binary string of n with exactly num_digits."""
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    return '0' * (num_digits - len(result)) + result
