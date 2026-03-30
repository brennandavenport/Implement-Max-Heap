def test_interleaved_operations(heap_cls):
    heap = heap_cls()

    for value in [10, 50, 20]:
        heap.push(value)

    assert heap.pop() == 50, "expected first pop to return 50"

    for value in [100, 5, 75]:
        heap.push(value)

    actual = [heap.pop(), heap.push(60), heap.pop(), heap.pop()]
    expected = [100, None, 75, 60]

    assert actual == expected, f"expected {expected}, got {actual}"
