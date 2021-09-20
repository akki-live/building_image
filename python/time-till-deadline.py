from datetime import datetime


user_input = input("enter you goal with a deadline  separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
try:
    deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

    today_date = datetime.today()

    time_till = deadline_date - today_date

    print(f"Dear user! Time reamining for you goal: {goal} is {int(time_till.total_seconds()/60/60)} hours")
except:
    print("Something is wrong with the code, please check ")