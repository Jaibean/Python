# -*- coding: utf-8 -*-
#
# Python Ver:   3.6
#
# Author:       Jaimie Bertoli
#
# Purpose:      Create a script that will find out the current times in the Portland HQ and NYC and London branches.
# Then, compare that time with each branch's hours to see if they are open or closed
#



import datetime
import pytz
from datetime import datetime, timezone
from pytz import timezone


pdx = pytz.timezone('America/Vancouver')

nyc = pytz.timezone('America/New_York')

portland_current_time = datetime.now(pdx).time()

nyc_current_time = datetime.now(nyc).time()

timeStart = 9
timeEnd = 17

         
if portland_current_time.hour >= timeStart and portland_current_time.hour < timeEnd:
    print("The Portland branch is open")
else:
    print("The Portland branch is closed")

if nyc_current_time.hour >= timeStart and nyc_current_time.hour < timeEnd:
    print("The NYC branch is open")
else:
    print("The NYC branch is closed")

