def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    mashq = {}
    x = 0
    i = 0
    k = 'LETTERS'
    while i <= len(txt)-1:
        if txt[i].isalpha():
            x += 1
        i+=1
    mashq[k]=x
    y = 0
    ix = 0
    l = 'DIGITS'
    while ix <= len(txt)-1:
        if txt[ix].isdigit():
            y += 1
        ix+=1
    mashq[l]=y

    return mashq
print(count_all("Hello World"))