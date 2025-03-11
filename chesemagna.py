#!/usr/bin/env python3

import csv
import time
from os.path import realpath
from pathlib import Path
from sys import argv

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
    rv = time.strftime('%W', date)
    if rv[0:1] == '0':
        rv = rv[1:]
    return int(rv)

def findMenuFile(menuWeek):
    weekFile = f'sett{menuWeek}.csv'
    for searchIn in ['.', realpath(__file__), f'{str(Path.home())}/docs' ]:
        fullPath = Path(f'{searchIn}/chesemagna-data/{weekFile}')
        if fullPath.exists() and fullPath.is_file():
            return str(fullPath)
    raise FileNotFoundError(f'Could not find {weekFile}')

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
if len(argv) <= 1:
    date = time.localtime()
else:
    date = time.strptime(argv[1], dateFormat)
weekday = int(time.strftime('%u', date)) # Monday = 1. Sunday = 7
weekNow = getWeekNum(date)

# calculate current menu week
weekRef = getWeekNum(dayRef)

# difference is base 0 but menu week is base 1
menuWeek = (weekNow - weekRef + weekMenuRef - 1) % cycleLen + 1

print(f'---- GIORNO {time.strftime(dateFormat, date)} ----')
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
