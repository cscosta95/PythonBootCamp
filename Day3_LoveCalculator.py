print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()
count1 = 0
count2 = 0

count1 += name1_lower.count("t")
count1 += name1_lower.count("r")
count1 += name1_lower.count("u")
count1 += name1_lower.count("e")
count1 += name2_lower.count("t")
count1 += name2_lower.count("r")
count1 += name2_lower.count("u")
count1 += name2_lower.count("e")

count2 += name1_lower.count("l")
count2 += name1_lower.count("o")
count2 += name1_lower.count("v")
count2 += name1_lower.count("e")
count2 += name2_lower.count("l")
count2 += name2_lower.count("o")
count2 += name2_lower.count("v")
count2 += name2_lower.count("e")

if count1 > 0 and count2 > 0:
    score = (count1 * 10) + count2
elif count1 == 0:
    score = count2
else:
    score = count1 * 10

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")