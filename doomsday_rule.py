#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Script that implements the doomsday rule, a way to calculate the day of the 
week for a given date. See https://en.wikipedia.org/wiki/Doomsday_rule
"""

import sys

NUM_ARGS = 4

YEARS_CYCLE = 400
DAYS_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MIN_MONTH = 1
MAX_MONTH = 12
MIN_YEAR = 1800
MAX_YEAR = 2199

ANCHOR_DAY = [ 5, 3, 2, 0 ]

NAME_OF_DAY_CONV = [ "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" ]
MEM_DATE = [ 3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12 ]
MEM_DATE_LEAP = [ 4, 29 ] + MEM_DATE[2:]

def adjust_year(year):
    """The calculation is only for years between 1800 and 2199. So for other
    years, adjust the year to this range knowing that these calculations are
    the same for years separated 400 years.
    """
    
    year_int = int(year)
    
    if year_int < MIN_YEAR:
        cycle = YEARS_CYCLE
    else:
        cycle = - YEARS_CYCLE 
    
    while not ( MIN_YEAR <= year_int <= MAX_YEAR ):
        year_int += cycle
        
    return str(year_int)

def check_date(day, month, year):
    """Check the date received."""
    
    check_ok = True
    
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    if not ( MIN_YEAR <= year_int <= MAX_YEAR ):        
        print "The year must be between %d and %d" % (MIN_YEAR, MAX_YEAR)
        check_ok = False
    elif not ( MIN_MONTH <= month_int <= MAX_MONTH ):
        print "The month must be between %d and %d" % (MIN_MONTH, MAX_MONTH)
        check_ok = False
    else:
        max_month = DAYS_MONTH[month_int - 1]
        
        if month_int == 2 and leap_year(year_int):
            max_month = 29
                       
        if not ( 1 <= day_int <= max_month ):
            print "The day must be between %d and %d" % (1, max_month)
            check_ok = False
        
    return check_ok

def leap_year(year):
    """ Multiplier of 4 not of 100 but yes 400.
    """
    
    return ( year % 4 == 0 and not year % 100 == 0 ) or year % 400 == 0

def doomsday_rule(year):
    """Just apply the doomsday rule. """
    
    year_2_last = int(year[-2:])
    
    a, b = divmod(year_2_last, 12)
    c = b // 4
    
    doomsday = (a + b + c + ANCHOR_DAY[int(year[:2]) - 18]) % \
        len(NAME_OF_DAY_CONV)        
    
    return doomsday

def main(day, month, year):
    
    new_year = adjust_year(int(year))
    
    if check_date(day, month, new_year):
    
        doomsday = doomsday_rule(new_year)
        
        # Calculations to get the day of the week from the doomsday day
        # depending on the day and month.
        if leap_year(int(year)):
            mem_date = MEM_DATE_LEAP
        else:
            mem_date = MEM_DATE
            
        day_ref = mem_date[int(month) - 1]
        
        day_int = int(day)
        
        if day_int < day_ref:
            the_day = (doomsday - day_ref + day_int) % len(NAME_OF_DAY_CONV)        
        elif day_int > day_ref:
            the_day = (doomsday + day_int - day_ref) % len(NAME_OF_DAY_CONV)    
        else:
            the_day = doomsday
        
        if doomsday >= 0:    
            print "Date (d/m/y): %s/%s/%s is %s" % \
                (day, month, year, NAME_OF_DAY_CONV[the_day])
        else:
            print "Doomsday calculated not valid."

if __name__ == "__main__":
    
    if len(sys.argv) != NUM_ARGS:
        print"ERROR: Need some arguments. Use: %s day month year" % sys.argv[0]
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])