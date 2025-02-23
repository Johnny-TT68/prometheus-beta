from typing import List, Tuple, Union

def lz78_compress(input_string: str) -> List[Tuple[int, str]]:
    """
    Implement the LZ78 compression algorithm.
    
    Args:
        input_string (str): The input string to compress
    
    Returns:
        List[Tuple[int, str]]: Compressed representation as list of (index, character) pairs
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary and compressed output
    dictionary = {
        '': 0  # Empty string starts with index 0
    }
    compressed = []
    current_sequence = ''
    
    # Iterate through each character in the input string
    for char in input_string:
        # Try to find the longest matching sequence
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If sequence exists, continue building it
            current_sequence = test_sequence
        else:
            # Get the index of the previous matching sequence
            previous_index = dictionary.get(current_sequence, 0)
            
            # Add new entry to compressed output
            compressed.append((previous_index, char))
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = len(dictionary)
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle last sequence if exists
    if current_sequence:
        previous_index = dictionary.get(current_sequence, 0)
        compressed.append((previous_index, ''))
    
    return compressed

def lz78_decompress(compressed: List[Tuple[int, str]]) -> str:
    """
    Decompress an LZ78 compressed representation.
    
    Args:
        compressed (List[Tuple[int, str]]): Compressed representation
    
    Returns:
        str: Decompressed original string
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If tuples do not match expected format
    """
    # Input validation
    if not isinstance(compressed, list):
        raise TypeError("Input must be a list of tuples")
    
    if not all(isinstance(entry, tuple) and len(entry) == 2 
               and isinstance(entry[0], int) and isinstance(entry[1], str) 
               for entry in compressed):
        raise ValueError("Invalid compressed format")
    
    # Initialize dictionary and result
    dictionary = {0: ''}
    result = []
    next_index = 1
    
    # Decompress each entry
    for index, char in compressed:
        # Get the previous sequence
        previous_sequence = dictionary.get(index, '')
        
        # Build new sequence
        new_sequence = previous_sequence + char
        result.append(new_sequence)
        
        # Add to dictionary if not empty
        if new_sequence:
            dictionary[next_index] = new_sequence
            next_index += 1
    
    return ''.join(result)