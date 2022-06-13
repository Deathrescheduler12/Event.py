AUTHOR'S MESSAGE = Sorry for leaving out the ambiguities


**EVENT PY:**

 *-*-*
Words that are commonly misunderstood:
etc = et cetera (which means "so on" or "and more"), 
u = You, 
ur = Your,
i.e = for example,
*not a word but*,
local system = a group that is more important than any other groups (not just a group but it's a specific group of beings that are capable of causing an event),
*-*-*

What is an event?

an event is something that happens with respect to position and time. Events can be "A guy falling off a tree"  or "A woman who's drinking coffee".
Events must obey two rules:
1) an event must be occuring at a position 

2) an event must be occuring at a specific time

These rules are unavoidable because they define the word "event" so if u decide to defy one of the rules then
the event is not EVENT but something else.
There are alot of types of event but the two types that we are gonna emphasize are:

1) External event (also called "Global event")

2) Internal event (also called "Local event")

External event.

This event takes place in a global scale. Given an example, a family being affected by the conditions in their country is an external event.

External events can be easy  to identify since it introduces a new *thing* in your local system (i.e family, city population and etc).
while it's easy to identify external events but sometimes it's not, if the affect is huge in magnitude then
you will face some difficulties, for example; 120 people killing twice their number of people in your local system,
it's difficult to keep track on the deceased ones along with those that have caused their death hence it's difficult.

Internal event.

This event takes place in a local system. Given an example, a girl in ur local system arguing with another girl in ur local system.
Internal events can be easy to identify since the events are occuring in ur local system.

Event transition.

This is a process where an event transitions from one type of an event to another, for example; a guy joining ur local system.
That guy is leaving the global scale (Global system) and is joining the local scale (local system)
As you might guess, event transition can be divided into two:
1) Global to Local

2) Local to Global

The previous example can be classified as "Global to Local" transition since an external object has left the global scale and joined the local scale.

Python events.

Here's how to make a simple event object

```py
from event import event
cycling = event(name = "batman", bike = {"number of wheels" : 2, "name of the bike" : "2xrcs"})
```

and here's how to close an event

```py
cycling.close_event()
```

*Remember a good event object must have alot of info*

what if im making alot of events?

You can use EventSeq which is basically a list but exclusively for events

```py
from utils import EventSeq
from event import event
cycling = event(action = "cycling", going_to = "local shop", reason = "To buy food", info = {"name" : "batman", "age" : 17})
seq = EventSeq(
    cycling, 
    event(action = "fell down", location = "the playground"), 
    event(action = "went black", location = "hospital"), 
    event(action = "died while struggling with my pain", location = "hospital"), 
    event(action = "people around my grave were grieving", location = "local cemetry")
)
```
which you can output the event list by doing this

```py
print(seq.sequence()) or print(seq[:])

>> EventSeq("EventInfo({'action': 'cycling', 'going_to': 'local shop', 'reason': 'To buy food', 'info': {'name': 'batman', 'age': 17}})", "EventInfo({'action': 'fell down', 'location': 'the playground'})", "EventInfo({'action': 'went black', 'location': 'hospital'})", "EventInfo({'action': 'died while struggling with my pain', 'location': 'hospital'})", "EventInfo({'action': 'people around my grave were grieving', 'location': 'local cemetry'})")
```

how do i access the information associated with the event object?

```py
from event import event
cycling = event(action = "cycling", going_to = "local shop", reason = "To buy food", info = {"name" : "batman", "age" : 17})
print(cycling.data.action) 

>> cycling
```

and there's also a way to manipulate the event list

let's take the previous example
```py
print(seq["skip [1] if [2].action == fell down"]) # it will skip the first element if the conditional expression is true
```

keyword: delete, skip ("halt" will be coming soon :) )

**I'm bored so hit me up! discord: Batman.#7438**

*You can also contribute if u want*
