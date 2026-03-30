def test_negative_numbers(heap_cls):
    heap = heap_cls()
    values = [-5, -1, -10, -2]

    for value in values:
        heap.push(value)

    actual = [heap.pop() for _ in range(len(values))]
    expected = [-1, -2, -5, -10]

    assert actual == expected, f"expected {expected}, got {actual}"
