import hw2_debugging

def test_mergeSort():
    assert hw2_debugging.mergeSort([6, 11, 7, 5, 8, 20, 5, 10, 19, 11, 7, 9, 14, 11, 20, 4, 5, 8, 10, 14]) == [4, 5, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 11, 14, 14, 19, 20, 20]
    assert hw2_debugging.mergeSort([4, 13, 4, 20, 17, 13, 9, 1, 5, 6, 13, 9, 7, 18, 7, 6, 18, 11, 4, 9]) == [1, 4, 4, 4, 5, 6, 6, 7, 7, 9, 9, 9, 11, 13, 13, 13, 17, 18, 18, 20]
    assert hw2_debugging.mergeSort([2, 8, 19, 13, 5, 20, 12, 20, 17, 15, 20, 7, 2, 16, 10, 13, 3, 17, 4, 9]) == [2, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 13, 15, 16, 17, 17, 19, 20, 20, 20]