"""
Countdown
"""

import sevseg, os
from time import sleep

def get_time(type: str) -> int:
    """Get time from user

    Args:
        type (str): "Hours", "Minutes", or "Seconds"

    Returns:
        int: time from user
    """
    print("Enter", type)
    start_time = input(">")

    while not start_time.isnumeric() and start_time < 0:
        print("Please enter a valid positive number")   
    
    return int(start_time)

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
        
# Get hours, minutes and seconds from user
hours = get_time("Hours")
minutes = get_time("Minutes")
seconds = get_time("Seconds")

# Start countdown
try:
    for hour in range(hours, -1, -1):
        for minute in range(minutes, -1, -1):
            for second in range(seconds, -1, -1):
                display_time(hour, minute, second)
                sleep(1)
            
            if minute == 0:
                minutes = 59
            
            if second == 0:
                seconds = 59
        
except KeyboardInterrupt:
    pass

print("** BOOM **")