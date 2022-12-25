def first_item(data):
    """
    Given a dictionary, Return first item value.
    """
    data = {'a': 1, 'b': 2}
    x = 0
    while data:
        key, value = data.popitem()
        x = value
    return x
print(first_item({'a': 1, 'b': 2}))