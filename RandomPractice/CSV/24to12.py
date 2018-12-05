from datetime import datetime
    
def convert(time: str) -> str:

    #check to see if time is in 24 hour format
    #if it is, convert it to 12 hour format
    if ((time[0] > 1) or (time[1] > 2)):
        new = datetime.strptime(time, "%H:%M")
        new.strftime("%I:%M %p")
    elif (time[0] <
