def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    i = 0
    a = {}
    while i <= len(cities)-1:
        a[i] = cities[i]
        i += 1
    return a
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))