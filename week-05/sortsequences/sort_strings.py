from datastubs import STRING_LIST

def reverse_alpha():
    return sorted(STRING_LIST, reverse=True)

def alpha_case_insensitive():
    def insensitive(s):
        return s.upper()
    return sorted(STRING_LIST, key=insensitive)

def by_longest_length():
    """
    Sort in descending order of length of strings
    """
    # fill it out
    def getLength(s):
        return len(s)
    return sorted(STRING_LIST, key=getLength, reverse=True)


def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)

    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/
    """
    # fill it out
    tempList = []
    for s in STRING_LIST:
        if (s.isnumeric()) == True:
            tempList.append(s)
    return sorted(tempList)


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order
    """
    # fill it out
    tempList = []
    for s in STRING_LIST:
        if (s.isnumeric()) == True:
            tempList.append(int(s))
    return sorted(tempList)



