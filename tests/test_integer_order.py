def test_integer_order(heap_cls):
    heap = heap_cls()
    values = [10, 20, 5, 15, 30, 25]

    for value in values:
        heap.push(value)

    actual = [heap.pop() for _ in range(len(values))]
    expected = [30, 25, 20, 15, 10, 5]

    assert actual == expected, f"expected {expected}, got {actual}"
