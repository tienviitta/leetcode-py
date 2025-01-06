cache = {}


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = value
        return value


def test_ex1():
    assert fibonacci(5) == 5


if __name__ == "__main__":
    test_ex1()
