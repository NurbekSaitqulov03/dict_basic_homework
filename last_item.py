def last_item(data):
    """
    Given a dictionary, Return last item value.
    """
    data = {'a': 1, 'b': 2}
    return data.get('b', 'not')
print(last_item({'a': 1, 'b': 2}))