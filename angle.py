import math


def dotproduct(v1, v2):
    """Dotproduct of two vectors.

    Args:
        v1 (iterable)
        v2 (iterable)

    Returns:
        scalar
    """
    return sum((a * b) for a, b in zip(v1, v2))


def length(v):
    """Length of a vector.

    Args:
        v (iterable)

    Returns:
        scalar
    """
    return math.sqrt(dotproduct(v, v))


def angle(v1, v2):
    """Angle between two vectors.

    Args:
        v1 (iterable)
        v2 (iterable)

    Returns:
        # scalar
    """
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
