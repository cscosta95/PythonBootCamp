# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
actual_age = int(age)

days_left = 365 * 90 - actual_age * 365
weeks_left = 52 * 90 - actual_age * 52
months_left = 12 * 90 - actual_age * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")