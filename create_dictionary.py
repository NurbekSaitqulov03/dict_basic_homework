def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    i = 0
    a = {}
    while i < len(key) and i < len(value):
        a[key[i]] = value[i]
        i+=1
    return a
print(create_dictionary([1, 2, 3], ["one", "two", "three"]))