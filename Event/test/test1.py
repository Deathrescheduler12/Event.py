import os
import sys
sys.path.append(os.path.join(os.getcwd()[:-5]))
from utils import EventSeq
from event import event
import time
events = EventSeq(event(speed = 10), event(speed = "None"), event(speed = 22), event(speed = 28))
print(events[:, "delete [3] if [2].speed == None"])




    



