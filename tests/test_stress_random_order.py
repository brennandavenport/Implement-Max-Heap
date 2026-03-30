import random


def test_stress_random_order(heap_cls):
    heap = heap_cls()
    values = [random.randint(0, 100000) for _ in range(10000)]

    for value in values:
        heap.push(value)

    actual = [heap.pop() for _ in range(len(values))]
    expected = sorted(values, reverse=True)

    assert actual == expected, "expected popped values to be sorted in descending order"
