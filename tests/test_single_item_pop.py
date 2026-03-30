def test_single_item_pop(heap_cls):
    heap = heap_cls()

    heap.push(42)

    assert heap.pop() == 42, "expected single pop to return the inserted value"
    assert heap.pop() is None, "expected heap to be empty after removing the only value"
