def first_item(data):
    """
    Given a dictionary, Return first item value.
    """
    data = {'a': 1, 'b': 2}
    return data.get('a', 'not')
print(first_item({'a': 1, 'b': 2}))