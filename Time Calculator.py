def add_time(start, duration,start_day=''):
    ndays = 0
    hours = 0
    minutes = 0
    before_midday = ' AM'
    after_midday = ' PM'
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    new_time = ''


    start = start.split()
    _M = start[1] #AM or PM
    start = start[0].split(':')
    duration = duration.split(':')
    if _M == 'PM' and start[0] != '12':
        hours += 12
    hours += int(start[0]) + int(duration[0])
    minutes += int(start[1]) + int(duration[1])

# Make sure it is time format
    while minutes >= 60:
        hours += 1
        minutes -= 60
    while hours >= 24:
        ndays += 1
        hours -= 24

# Time format for minutes       
    if minutes < 10:
        minutes = '0'+str(minutes)
    else:
        minutes = str(minutes)

# Midday or not
    if 0 < hours < 11:
        new_time += str(hours) + ':' + minutes + before_midday
    elif hours == 0:
        hours += 12
        new_time += str(hours) + ':' + minutes + before_midday
    elif hours > 12:
        hours -= 12
        new_time += str(hours) + ':' + minutes + after_midday

#Days of the week
    if not start_day == '':
        start_day = start_day.lower()
        d = days.index(start_day) #What day is it
        ds = (d + ndays) % 7
        new_time += ', ' + days[ds][0].upper() + days[ds][1:len(days[ds])]

# How many days
    if ndays == 1:
        new_time += ' (next day)'
    elif ndays > 1 :
        new_time += f' ({ndays} days later)'

    print(new_time)
    return new_time

add_time('11:59 AM', '0:01', 'Monday')
