#!/bin/python
# Prayer day

# For using configuration/global variables
from Config import * 

# For stroing the dates and times fo the prayers
import datetime

import DL
import sys

if City == "":
    sys.stderr.write("The city has not been entered. Put in the City in Config.py\n")
    sys.stderr.write("Use https://prayertimes.date/api/docs/cities to get the name of the city, than put it in the City variable\n")
    sys.exit(2)

# Should not be changed: only chagne in DL
PRAYER_MAP=DL.load()


def getDay(year, month, day):
    date = datetime.datetime(year, month, day)
    today = datetime.datetime.today()
    temp = datetime.datetime(today.year, today.month, today.day)

    if( date>= temp ):
        try:
            return PRAYER_MAP[datetime.datetime(year, month, day)]
        except KeyError:
            DL.save()
            return PRAYER_MAP[datetime.datetime(year, month, day)]
    else:
        sys.stderr.write("Date in past, cannot do that. If demand I'll add it")
        sys.exit(2)

def nextPrayer():
    now = datetime.datetime.today()
    today = getDay(now.year, now.month, now.day)
    for prayer in prayers:
        if( today[prayer] > now):
            return (prayer, today[prayer].strftime("%H:%M"))

    

print( nextPrayer() ) 
