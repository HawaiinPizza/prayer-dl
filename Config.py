# Configuration
import datetime

# File to save the prayers at
File="/home/zaki/Projects/Programm/Prayer-dl/.Prayers.pickle"

# Interval to get new prayers

# Website to get data from https://prayertimes.date/api/docs/cities
# TODO see if using enum is an appoeriate hcoice
from enum import Enum
class Interval(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 4

TimeInterval=Interval.WEEKLY

_city_prefix="?city="
City=_city_prefix+"Dearborn"

# 
# prayer_map = {None : None}
prayer_map = {}

# API specific.  Use to get the values in prayer by parsing the jason
prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
