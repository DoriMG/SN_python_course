def sum_numbers(n):
    if n is None:
        return None
    if type(n) is not int:
        raise TypeError()
    if n <= 0:
        return 0
    return sum(list(range(n+1)))
