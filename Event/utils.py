from error import EventSeqImmutable
from constants import EVENTSEQIMMUTABLE
from parser import *
def get_state(conditional, req, opfunc):
    return opfunc(conditional, req)
def change_str(seq, name):
    if isinstance(seq, tuple) or isinstance(seq, list):
        seq = [x.call() for x in seq]
        result = str(seq)[1:-1]
    elif isinstance(seq, str):
        result = seq
    else:
        raise TypeError("This function only accepts non-homogenous sequences or string literals")
    return f"{name}({result})"
class EventSeq:
    def __init__(self, *elements):
        self.elements = [x for x in elements]
    def __getitem__(self, n):
        new_list = self.elements
        if isinstance(n, int):
            return self.elements[n].call()
        if isinstance(n, tuple):
            for x in n:
                if isinstance(x, slice):
                    new_list = self.elements[x]
                elif isinstance(x, str):
                    keyword = parse_keywords(x)[0]
                    operator, opfunc = parse_operation(x)
                    action = parse_element(x[:x.find("if")])
                    conditional = parse_element(x[x.find("if"):])
                    required = parse_req(x)
                    pass
                else:
                    return None
        elif isinstance(n, str):
            keyword = parse_keywords(n)[0]
            operator, opfunc = parse_operation(n)
            action = parse_element(n[:n.find("if")])
            conditional = parse_element(n[n.find("if"):])
            required = parse_req(n)
            pass
        elif isinstance(n, slice):
            return change_str(self.elements[n], "EventSeq")
        if action["element"] == "all":
            return None
        if conditional["element"] == "all":
            check = []
            for x in new_list:
                data = getattr(x, "data")
                check.append(opfunc(getattr(data, conditional["method"]), int(required) if required.isdigit() else required))
            if all(check) == True:
                state = True
            else:
                state = False
            del check
        else:
            data = getattr(new_list[int(conditional["element"]) - 1], "data")
            state = opfunc(getattr(data, conditional["method"]), int(required) if required.isdigit() else required)
        if state:
            element = int(action["element"])
            if keyword == "skip":
                return change_str(skip(new_list[element - 1], new_list), "EventSeq")
            if keyword == "delete":
                new = skip(new_list[element - 1], new_list)
                for x in self.elements:
                    if x not in new:
                        del self.elements[self.elements.index(x)]
                    else:
                        continue
                return change_str(self.elements, "EventSeq")
            if keyword == "halt":
                return "New implementations are coming soon"
        else:
            return change_str(new_list, "EventSeq")
    def __setitem__(self, n, value):
        raise EventSeqImmutable(EVENTSEQIMMUTABLE)
    def sequence(self):
        return change_str(self.elements, "EventSeq")
def eventtype(func):
    return func.__eventtype__()