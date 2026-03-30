def test_push_updates_peek(heap_cls):
    heap = heap_cls()

    heap.push(10)
    heap.push(40)
    heap.push(25)

    assert heap.peek == 40, f"expected peek to be 40, got {heap.peek}"
