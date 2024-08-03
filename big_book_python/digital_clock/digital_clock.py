"""
Digital Clock
"""

import sevseg, os
import datetime
from time import sleep

def display_time(hours: int, minutes: int, seconds: int):
    """Display time to screen HH:MM:SS
    """
    os.system('cls')
    formatted_time = """"""
    
    split_hours = sevseg.getSevSegStr(hours, 2).splitlines()
    split_minutes = sevseg.getSevSegStr(minutes, 2).splitlines()
    split_seconds = sevseg.getSevSegStr(seconds, 2).splitlines()
    
    for line in range(0, 3):
        formatted_time += split_hours[line]
        
        if line == 0:
            formatted_time += "   "
        else:
            formatted_time += " * "
            
        formatted_time += split_minutes[line]
        
        if line == 0:
            formatted_time += "   "
        else:
            formatted_time += " * "
            
        formatted_time += split_seconds[line]
        formatted_time += "\n"
        
    formatted_time = formatted_time.splitlines()    
    for line in formatted_time:
        print(line)
    
    print("\nPress Ctrl+C to quit.")


current_time = datetime.datetime.now()
hours = int(current_time.strftime("%H"))
minutes = int(current_time.strftime("%M"))
seconds = int(current_time.strftime("%S"))

try:
    while True:
        for minute in range(minutes, 59):
            for second in range(seconds, 59):
                display_time(hours, minute, second+1)
                sleep(1)
            
            seconds = 0
        
        minutes = 0
        current_time = int(datetime.datetime.now())
        hours = current_time.strftime("%H")
        
except KeyboardInterrupt:
    pass
