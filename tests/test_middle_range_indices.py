import pytest
from src.middle_range_indices import get_middle_range_indices

def test_odd_length_list_default_range():
    """Test middle range indices for odd-length list with default range size"""
    test_list = [1, 2, 3, 4, 5]
    assert get_middle_range_indices(test_list) == [2]

def test_even_length_list_default_range():
    """Test middle range indices for even-length list with default range size"""
    test_list = [1, 2, 3, 4, 5, 6]
    assert get_middle_range_indices(test_list) == [2]

def test_custom_range_size():
    """Test middle range indices with a custom range size"""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_middle_range_indices(test_list, range_size=2) == [3, 4, 5]

def test_range_size_zero():
    """Test middle range indices with range size of zero"""
    test_list = [1, 2, 3, 4, 5]
    assert get_middle_range_indices(test_list, range_size=0) == [2]

def test_large_range_size():
    """Test middle range indices with range size larger than list"""
    test_list = [1, 2, 3, 4, 5]
    assert get_middle_range_indices(test_list, range_size=10) == [0, 1, 2, 3, 4]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_middle_range_indices("not a list")
    
    with pytest.raises(TypeError, match="Range size must be an integer"):
        get_middle_range_indices([1, 2, 3], range_size="invalid")

def test_negative_range_size():
    """Test error handling for negative range size"""
    with pytest.raises(ValueError, match="Range size cannot be negative"):
        get_middle_range_indices([1, 2, 3], range_size=-1)

def test_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        get_middle_range_indices([])