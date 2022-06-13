from error import EventClosed, EventImmutable
from constants import EVENTCLOSED, EVENTIMMUTABLE
from utils import EventSeq
from typing import NewType
# warning: Events aren't completely immutable
class EventInfo(object):
    def __init__(self, data):
        self.data = data
        for keys, values in data.items():
            if isinstance(values, str):
                exec(f"self.{keys} = '{values}'")
            else:
                if isinstance(values, dict):
                    exec(f"self.{keys} = func", {"func" : EventInfo(values), "self" : self})
                else:
                    exec(f"self.{keys} = {values}")
    def read(self):
        return "EventInfo(" + str(self.data) + ")"
class event:
    __slots__ = ["__data", "isfinished"]
    def __init__(self, **__data):
        self.__data = EventInfo(__data)
        self.isfinished = False
    @property
    def data(self):
        if self.isfinished == True:
            raise EventClosed(EVENTCLOSED)
        else:
            return self.__data
    @data.setter
    def data(self):
        raise EventImmutable(EVENTIMMUTABLE)
    def call(self):
        return self.__data.read()
    def log(self, **data):
        if self.isfinished:
            raise EventClosed(EVENTCLOSED)
        else:
            self.__data = EventInfo(data)
    def close_event(self):
        self.isfinished = True
cycling = event(action = "cycling", going_to = "local shop", reason = "To buy food", info = {"name" : "mohamed", "age" : 17})
seq = EventSeq(
    cycling, 
    event(action = "fell down", location = "the playground"), 
    event(action = "went black", location = "hospital"), 
    event(action = "died while struggling with my pain", location = "hospital"), 
    event(action = "people around my grave were grieving", location = "local cemetry")
)
print(seq["skip [1] if [2].action == fell  down"])