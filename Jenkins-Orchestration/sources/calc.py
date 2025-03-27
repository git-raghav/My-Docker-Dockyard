def add2(val1, val2):
    """
    Add two values. If either value is a string, treat both as strings and concatenate.
    Otherwise, perform numeric addition.
    """
    try:
        # Try numeric addition first
        return float(val1) + float(val2)
    except (ValueError, TypeError):
        # If numeric addition fails, concatenate as strings
        return str(val1) + str(val2) 