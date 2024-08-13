import pytest
from bubble_sort import select_index

def test_small_list ():
    test_list = [5,4,2,1,3]
    result= select_index(test_list)
    print (result)
    assert result == [1, 2, 3, 4, 5]

def test__big__list ():
    test_list = [57, 1, 84, 39, 99, 13, 70, 33, 6, 95, 23, 81, 45, 17, 78, 54, 9, 88, 60, 30, 98, 15, 65, 3, 51, 92, 12, 72, 48, 20, 37, 77, 7, 100, 27, 89, 43, 18, 68, 35, 62, 25, 82, 5, 90, 40, 16, 97, 50, 2, 73, 61, 21, 10, 66, 34, 74, 19, 55, 42, 86, 11, 96, 32, 71, 56, 22, 8, 91, 28, 44, 93, 14, 67, 52, 38, 79, 4, 87, 59, 29, 46, 76, 26, 85, 63, 0, 94, 36, 83, 41, 58, 47, 75, 64, 31, 80, 49, 24, 53, 69]
    result= select_index(test_list)
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def test_empty_list():
    test_list = []
    with pytest.raises(AttributeError):
        select_index(test_list)

def test_no_list():
    no_test_list = 5
    with pytest.raises(ValueError):
        select_index(no_test_list)