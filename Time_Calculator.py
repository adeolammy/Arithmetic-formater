def add_time(start_time, duration, starting_day=None):
    # Parse the start time
    start_time, meridian = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate the total minutes
    total_minutes = start_hour * 60 + start_minute
    
    if meridian == 'PM':
        total_minutes += 12 * 60
    
    total_minutes += duration_hour * 60 + duration_minute
    
    # Calculate the final time and days later
    days_later = total_minutes // (24 * 60)
    final_minutes = total_minutes % (24 * 60)
    
    final_hour = final_minutes // 60
    final_minute = final_minutes % 60
    
    # Determine AM/PM
    if final_hour >= 12:
        meridian = 'PM'
        if final_hour > 12:
            final_hour -= 12
    else:
        meridian = 'AM'
        if final_hour == 0:
            final_hour = 12
    
    # Determine the day of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        starting_index = days_of_week.index(starting_day)
        final_day_index = (starting_index + days_later) % 7
        final_day = days_of_week[final_day_index]
        days_later_text = f", {days_later} days later"
    else:
        final_day = ''
        days_later_text = ''
    
    # Format the final time
    final_time = f"{final_hour:02d}:{final_minute:02d} {meridian}"
    if days_later == 1:
        final_time += " (next day)"
    elif days_later > 1:
        final_time += f" ({days_later} days later)"
    
    # Append the day of the week if available
    if final_day:
        final_time += f", {final_day}"
    
    return final_time
print(add_time("3:00 PM", "3:10"))


print(add_time("11:30 AM", "2:32", "Monday"))


print(add_time("11:43 AM", "00:20"))


print(add_time("10:10 PM", "3:30"))


print(add_time("11:43 PM", "24:20", "tueSday"))


print(add_time("6:30 PM", "205:12")) 

