def is_int(
    value: str
    ) -> bool:
    """
    
    Checks if a value is an integer
    
    :param value: The value to check.
    :rtype: bool
    """
    try:
        value = float(value)
        if int(value) == value:
            value = int(value)
            return True
        else:
            return False
    except:
        return False
        
        
def is_float(
    value: str
    ) -> bool:
    """
    
    Checks if a value is a float.
    
    :param value: The value to check.
    :rtype: bool
    """
    try:
        if "." in list(value):
            value = float(value)
            return True
    except:
        return False
