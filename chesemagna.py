#!/usr/bin/env python3

import csv
import time

# config
dateFormat = '%Y-%m-%d' # YYYY-MM-DD ISO date format
dayRef = time.strptime('2025-01-27', dateFormat)
weekMenuRef = 3
cycleLen = 5
# ------

def getWeekNum(date):
    '''
    @brief Convert a date into a week number
    @param date The date to convert. type: struct_time
    @return week number: ranges from 0 to 53.
            1st Monday of the year is the 1st day with week numb. = 1
    '''
    return int(time.strftime('%-W', date))

def findMenuFile(menuWeek):
    # TODO implement
    return f'./chesemagna-data/sett{menuWeek}.csv'

def printMenu(header, values):
    for i in range(len(header)):
        print(header[i], end = '')
        values[i] = values[i].split('o ')
        # remove empty menu entries
        values[i] = [ x for x in values[i] if len(x) > 0 ]
        if len(values[i]) == 1:
            print(' ' + values[i][0])
        else:
            print()
            print(' - ' + '\n - '.join(values[i]))

# Analyze current day
now = time.localtime()
weekday = int(time.strftime('%u', now)) # Monday = 1. Sunday = 7
weekNow = getWeekNum(now)

# calculate current menu week
weekRef = getWeekNum(dayRef)

# difference is base 0 but menu week is base 1
menuWeek = (weekNow - weekRef + weekMenuRef - 1) % cycleLen + 1

print(f'---- GIORNO {time.strftime(dateFormat, now)} ----')
print(f'---- SETTIMANA {menuWeek}/{cycleLen} ----')

menuFile = findMenuFile(menuWeek)

header = []
values = []
with open(menuFile, 'r') as f:
    menu = csv.reader(f, delimiter=';')
    dayIdx = 1
    for record in menu:
        if len(header) == 0:
            header = record
        elif dayIdx < weekday:
            dayIdx += 1
        else:
            values = record
            break
printMenu(header, values)
