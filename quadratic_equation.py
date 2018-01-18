from math import sqrt


def get_roots_root1(discriminant, a, b):
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    return root1

def get_roots_root2(discriminant, a, b):
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root2


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        root1 = get_roots_root1(discriminant, a, b)
        return root1, None
    else:
        root1 = get_roots_root1(discriminant, a, b)
        root2 = get_roots_root2(discriminant, a, b)
        return root1, root2