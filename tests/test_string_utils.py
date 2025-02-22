import pytest
from src.string_utils import rotate_and_reverse

def test_rotate_and_reverse_basic():
    """Test basic rotation and reversal"""
    assert rotate_and_reverse("hello", 2) == "lohel"

def test_rotate_and_reverse_full_rotation():
    """Test rotation equal to string length"""
    assert rotate_and_reverse("hello", 5) == "olleh"

def test_rotate_and_reverse_beyond_length():
    """Test rotation more than string length"""
    assert rotate_and_reverse("hello", 7) == "ohell"

def test_rotate_and_reverse_zero_rotations():
    """Test zero rotations"""
    assert rotate_and_reverse("hello", 0) == "hello"

def test_rotate_and_reverse_empty_string():
    """Test empty string"""
    assert rotate_and_reverse("", 3) == ""

def test_rotate_and_reverse_negative_rotations():
    """Test negative rotation values"""
    assert rotate_and_reverse("hello", -2) == "ohell"

def test_rotate_and_reverse_single_char():
    """Test single character string"""
    assert rotate_and_reverse("a", 5) == "a"