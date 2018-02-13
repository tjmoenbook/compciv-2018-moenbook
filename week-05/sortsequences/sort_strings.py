from datastubs import STRING_LIST

def reverse_alpha():
    return sorted(STRING_LIST, reverse=True)

def alpha_case_insensitive():
    def insensitive(s):
        return s.upper()
    return sorted(STRING_LIST, key=insensitive)

def by_longest_length():
    def getLength(s):
        return len(s)
    return sorted(STRING_LIST, key=getLength, reverse=True)

def filter_and_sort_number_strings():
    tempList = []
    for s in STRING_LIST:
        if (s.isnumeric()) == True:
            tempList.append(s)
    return sorted(tempList)

def filter_and_sort_number_strings_as_numbers():
    tempList = []
    for s in STRING_LIST:
        if (s.isnumeric()) == True:
            tempList.append(s)
    return sorted(tempList,key=int)