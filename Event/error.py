class eventError(Exception):
    pass
class EventClosed(eventError):
    pass
class EventImmutable(eventError):
    pass
class EventSeqImmutable(eventError):
    pass
class DuplicateError(Exception):
    pass
class KeywordNotExist(Exception):
    pass