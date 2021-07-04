import datetime
# import string
# import random
# from django.utils.text import slugify

from .dateconverter import shamsiDate

def shamsi_date():
    now    = datetime.datetime.now()
    year   = now.year
    month  = now.month
    day    = now.day
    hour   = now.hour
    minute = now.minute
    second = now.second
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    if len(str(second)) == 1:
        second = "0" + str(second)
    stoday   = shamsiDate(int(year), int(month), int(day))
    clocknow = str(hour) +":"+ str(minute) +":"+ str(second)
    return f'{stoday} - {clocknow}'
