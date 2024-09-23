import time

print("Hello World")
time.sleep(1)
name = input("What is your name ?")
print("Hello " + name)
time.sleep(1.5)
print("My name is Alexa, and I am your personal study hours calculator")
time.sleep(2)
sleeping_hours = int(input("How many hours do you sleep everyday? "))
working_hours = int(
    input("How many hours do you work per day, including commute? "))
weekday_relaxing_hours = int(
    input("How many hours do you need to relax per day? "))
weekend_relaxing_hours = int(
    input("How many hours do you relax per weekend day ?"))
# compute availbe study hours
weekday_available_study_hours = 24 - sleeping_hours - working_hours - weekday_relaxing_hours - 3
weekend_available_hours = 24 - sleeping_hours - weekend_relaxing_hours - 3
total_available_hours = weekday_available_study_hours * 5 + weekend_available_hours
print("You have " + str(weekday_available_study_hours) +
      " study hours per day" + ", " + str(weekend_available_hours) +
      " study hours per weekend " + "and " + str(total_available_hours) +
      " study hours per week")


