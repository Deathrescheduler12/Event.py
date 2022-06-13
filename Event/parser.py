from error import DuplicateError, KeywordNotExist
from constants import ISDUPLICATE, KEYWORDNOTEXIST
from parsing_utils import *
def parse_operation(text):
    empty = ""
    words = []
    for x in text:
        if x == " ":
            words.append(empty)
            empty = ""
        else:
            empty += x
    for z in words:
        for j in operations:
            if z == j[0]:
                operation = j
            else:
                continue
    return operation
def parse_element(text):
    """
    ::text:: str

    Parses the conditional element
    """
    check = check_all(text)
    if check:
        element = "all"
        method = find(text, {"start" : "."})
    else:
        element = find(text, {"start" : "[", "end" : "]"}).strip()
        method = find(text, {"start" : "."})
    element = {"element" : element, "method" : method.strip() if method else method}
    return element
def parse_keywords(text):
    """
    ::text:: str

    Parses the keywords and stores them in a list
    """
    keywords = ['skip', 'delete', 'halt']
    store = []
    text = text.split()
    for x in text:
        for key in keywords:
            if x == key:
                store.append(x)
    if store:
        pass
    else:
        raise KeywordNotExist(KEYWORDNOTEXIST)
    check_duplicates(store)
    return store
def parse_req(x):
    z = parse_operation(x)
    return " ".join(x[x.find(z[0]):].split()[1:])

        

