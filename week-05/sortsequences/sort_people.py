from datastubs import PEOPLE_LIST

def longest_name():
    def getNameLength(nl): 
        return len(nl['name'])
    return sorted(PEOPLE_LIST, key=getNameLength, reverse=True)

def youngest():
    def getAge(a): 
        return a['age']
    return sorted(PEOPLE_LIST, key=getAge)

def oldest():
    def getAge(a): 
        return a['age']
    return sorted(PEOPLE_LIST, key=getAge, reverse=True)


def name_reverse_alpha():
    def getName(n)
        return n['name']
    return sorted(PEOPLE_LIST, key=getName, reverse=True)

def country_then_age():
    def getCountryAge(m):
        return (m['country'],m['age'])
    return sorted(PEOPLE_LIST, key=getCountryAge)