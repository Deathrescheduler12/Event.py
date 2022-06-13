from error import DuplicateError
from constants import ISDUPLICATE
def isgreater_or_equal(a, b) -> bool: # >=
    if a >= b:
        return True
    else:
        return False
def isless_or_equal(a, b) -> bool: # <=
    if a <= b:
        return True
    else:
        False
def equal(a, b) -> bool: # ==
    print(a, b)
    if a == b:
        return True
    else:
        return False
def notequal(a, b) -> bool: # !=
    if a != b:
        return True
    else:
        return False
def isgreater(a, b) -> bool: # >
    if a > b:
        return True
    else:
        return False
def isless(a, b) -> bool: # <
    if a < b:
        return True
    else:
        return False
def find(text, element):
    empty = ""
    words = []
    start = element.get("start")
    end = element.get("end")
    # i could have done .split() but i wanted to do in my way
    for x in text:
        if x == " ":
            words.append(empty)
            empty = ""
        else:
            empty += x
            continue
    for z in words:
        if start in z:
            word = z
        else:
            continue
    try:
        if start:
            word = word[word.find(start) + 1:]
        if end:
            word = word[:word.find(end)]
        else:
            pass
    except:
        word = None
    return word
def check_all(text):
    empty = ""
    words = []
    # i could have done .split() but i wanted to do in my way
    for x in text:
        if x == " ":
            words.append(empty)
            empty = ""
        else:
            empty += x
            continue
    for x in words:
        if "all" in x:
            return True
        else:
            continue
def check_duplicates(seq) -> None:
    """
    ::seq:: Tuple or List (non-homogeonous sequences)

    Looks for duplicates in the given sequence
    """
    for x in seq:
        if seq.count(x) > 1:
            raise DuplicateError(ISDUPLICATE)
        else:
            continue
def skip(element, sequence):
    """
    ::element:: str
    ::sequence:: Tuple or List (non-homogeonous sequences)


    Skips the given element from the sequence
    """
    new_seq = []
    # Another way of doing this is by using list comprehension
    for x in sequence:
        if x == element:
            continue
        else:
            new_seq.append(x)
    return new_seq
def halt(element, sequence):
    """
    ::element:: str
    ::sequence:: Tuple or List (non-homogeonous sequences)


    Halts the given element from the sequence (Aka placing it at the index of [-1])
    """
    new_seq = []
    for x in sequence:
        if x == element:
            continue
        else:
            new_seq.append(x)
    new_seq.insert(-1, element)
    return new_seq
# Operations used to evaluate the conditional
operations = [
    ("!>", isless_or_equal), 
    ("<!", isgreater_or_equal), 
    (">", isgreater), 
    ("<", isless), 
    (">=", isgreater_or_equal), 
    ("<=", isless_or_equal), 
    ("==", equal), 
    ("!=", notequal)
]