def test_string_order(heap_cls):
    heap = heap_cls()
    values = ["apple", "zebra", "banana", "cherry"]

    for value in values:
        heap.push(value)

    actual = [heap.pop() for _ in range(len(values))]
    expected = ["zebra", "cherry", "banana", "apple"]

    assert actual == expected, f"expected {expected}, got {actual}"
