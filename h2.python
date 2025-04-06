def decode_message(encoded):
    """
    Decodes the rover's encrypted message by reversing the shift pattern.
    
    Args:
        encoded (str): Encoded message (letters only)
        
    Returns:
        str: Decoded message in uppercase
    """
    decoded = []
    encoded = encoded.upper()  # Convert to uppercase
    
    for i, char in enumerate(encoded):
        shift = i + 1  # shifts start at 1 for first character
        original_ord = ord(char) - shift
        
        # Handle the alphabets (A comes after Z)
        if original_ord < ord('A'):
            original_ord += 26
            
        decoded_char = chr(original_ord)
        decoded.append(decoded_char)
    
    return ''.join(decoded)

if __name__ == "__main__":
    print(decode_message('NCUW'))  # Should print "MaRS"
