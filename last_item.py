def last_item(data:dict):
    """
    Given a dictionary, Return last item value.
    """
    data = {'a': 1, 'b': 2}
    key, value = data.popitem()
    return value
print(last_item({'a': 1, 'b': 2}))