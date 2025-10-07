# -------------------------------------------------
# Name: Navya Kumar
# Roll No: 2501410054
# Date: 7 October 2025
# Project: Daily Calorie Tracker
# -------------------------------------------------

import datetime

# Printing the banner
print("===========================================")
print("        Daily Calorie Tracker")
print("===========================================\n")

print("This program helps you keep track of your meals and total calorie intake.\n")
# Asking user for number of meals
meal_count = int(input("How many meals did you have today? "))

# Empty lists for storing values later
meal_names = []
meal_calories = []

# Loop to store n number of meals, (as entered by user)
for i in range(meal_count):
    print("\nMeal", i + 1)
    name = input("Enter meal name: ")
    cal = float(input("Enter calories for this meal: "))
    meal_names.append(name)
    meal_calories.append(cal)

# Calculating total and avg calories

total_calories = sum(meal_calories)
average_calories = total_calories / meal_count
# Asking for calorie limit
limit = float(input("\nEnter your daily calorie limit: "))
# Condition to check if the user exceeded the calorie limit or not
print("\n-------------------------------------------")
if total_calories > limit:
    print(f"You have exceeded your daily limit by {total_calories - limit}  calories.")
elif total_calories == limit:
    print("You have exactly reached your daily limit.")
else:
    print(f"You are within your daily limit by {limit - total_calories} calories.")
print("-------------------------------------------\n")

print("Today's Calorie Summary:\n")
print("Meal Name          Calories")
print("-------------------------------------------")

for i in range(len(meal_names)):
    spaces = " " * (20 - len(meal_names[i]))
    print(meal_names[i] + spaces + str(meal_calories[i]))

print("-------------------------------------------")
print("Total Calories:", total_calories)
print(f"Average per Meal:{average_calories}")
print("-------------------------------------------")

save = input("\nDo you want to save this report? (yes/no): ")

# Saving the data into a file

if save.lower() == "yes":
    file = open("daily_calorie_log.txt", "a")
    file.write("\n=== Daily Calorie Tracker Log ===\n")
    file.write("Date/Time: " + str(datetime.datetime.now()) + "\n")
    for i in range(len(meal_names)):
        file.write(meal_names[i] + " - " + str(meal_calories[i]) + " calories\n")
    file.write("Total: " + str(total_calories) + "\n")
    file.write(f"Average per Meal: {average_calories} \n")
    if total_calories > limit:
        file.write(f"Status: Over limit by{total_calories - limit} calories\n")
    elif total_calories == limit:
        file.write("Status: Exactly at limit\n")ṇ
    else:
        file.write(f"Status: Within limit {limit - total_calories} calories left\n")
    file.write("-------------------------------------------\n")
    file.close()
    print("\nReport saved successfully in daily_calorie_log.txt")

print("\nThank you for using the Daily Calorie Tracker!\n")
