def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotate the string by the specified number of rotations and then reverse it.
    
    Args:
        string (str): The input string to rotate and reverse
        rotations (int): Number of times to rotate the string
    
    Returns:
        str: The rotated and reversed string
    """
    # Handle empty string or zero rotations case
    if not string or rotations == 0:
        return string
    
    # Normalize rotations to be within string length
    effective_rotations = rotations % len(string)
    
    # Perform rotation
    rotated = string[effective_rotations:] + string[:effective_rotations]
    
    # Reverse the rotated string
    return rotated[::-1]