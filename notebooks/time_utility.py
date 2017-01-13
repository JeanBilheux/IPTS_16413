import os

def format_time_stamp(file_name = None, time_stamp = None):
    """Format the time stamp to easily retrieve the day, time, hour,
    and keep only short file name"""
    
    _short_file_name = os.path.basename(file_name)
    [week_day, month, day, hours, year] = time_stamp.split()
    
    [hours, minutes, seconds] = hours.split(':')
    _dict_time = {"hours": hours,
                  "minutes": minutes,
                  "seconds": seconds}
    
    _dict_time_stamp = {"week_day": week_day,
                       "month": month,
                       "day": day,
                       "hours": _dict_time,
                       "year": year}
    
    return [_short_file_name, _dict_time_stamp]