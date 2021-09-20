def days_to_units(num_of_days, unit_num):
    if unit_num == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {unit_num}"
    else:
        return f"{num_of_days} days are {num_of_days * 24 * 60} {unit_num}"




def validate_and_execute(days_and_unit_dictionary):
    
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        # this is to convert only positive number
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered zero , please check")
        else:
            print("you entered a negative number.....")
    except:
        print("your input is not a number, please check and enter a valid number..")