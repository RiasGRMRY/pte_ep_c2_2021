try:
    raw_input_data = input("Please give me a duratiob in secs: ")
    sum_of_secs = int(raw_input_data)
    if sum_of_secs < 0:
        print("Invapid Input!")
    elif sum_of_secs == 0:
        print("now")
    else:
        secs_in_min = 60
        secs_in_hour = 60 * secs_in_min
        secs_in_day = 24 * secs_in_hour
        secs_in_year = 365 * secs_in_day


        years = sum_of_secs // secs_in_year
        sum_of_secs = sum_of_secs - years * secs_in_year

        days = sum_of_secs // secs_in_day
        sum_of_secs = sum_of_secs - days * secs_in_day

        hours = sum_of_secs // secs_in_hour
        sum_of_secs = sum_of_secs - hours * secs_in_hour

        mins = sum_of_secs // secs_in_min
        secs = sum_of_secs - mins * secs_in_min

        number_of_units = 0
        if years > 0:
            number_of_units += 1
        if days > 0:
            number_of_units += 1
        if hours > 0:
            number_of_units += 1
        if mins > 0:
            number_of_units += 1
        if secs > 0:
            number_of_units += 1

        output = ""
        if years > 0:
            output += str(years) + " years"
            if years > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if days > 0:
            output += str(days) + " day"
            if days > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1
        if mins > 0:
            output += str(mins) + " mins"
            if mins > 1:
                output += "s"
            if number_of_units > 2:
                output += ", "
            elif number_of_units == 2:
                output += " and "
            number_of_units -= 1

except ValueError:
    print("Invalid input!")