# tracker.py
# Name: [shiva]
# Date: [1.11.2025]
# Project Title: Daily Calorie Tracker CLI

import datetime

print("Welcome to the Daily Calorie Tracker CLI Tool!")
print("Log your meals and calories, check your total intake, and compare to your personal daily limit.\n")

# Task 2: Input Data Collection
meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal = input(f"Enter meal {i+1} name: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Task 3: Calorie Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts)
calorie_limit = float(input("Enter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > calorie_limit:
    status_message = f"Warning: You have exceeded your daily calorie limit by {total_calories - calorie_limit:.2f} calories."
else:
    status_message = "Good job! You are within your daily calorie limit."

# Task 5: Neatly Formatted Output
print("\nMeal Name\tCalories")
print("----------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")
print("----------------------------")
print(f"Total\t\t{total_calories}")
print(f"Average\t\t{average_calories:.2f}")
print(status_message)

# Task 6: Bonus - Save Session Log to File
save_log = input("\nDo you want to save this session log to a file? (yes/no): ")
if save_log.lower() == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorielog.txt"
    with open(filename, 'w') as f:
        f.write(f"Calorie Tracker Log - {timestamp}\n")
        f.write("Meal Name\tCalories\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            f.write(f"{meal}\t\t{cal}\n")
        f.write("----------------------------\n")
        f.write(f"Total\t\t{total_calories}\n")
        f.write(f"Average\t\t{average_calories:.2f}\n")
        f.write(status_message + "\n")
    print(f"Session successfully saved to {filename}")
