#This is a BMI Calculator, the BMI is calculated by diving the weight by the height to an exponent of 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / (float(height)**2)
print(weight + " ÷ " + "(" + height + " x " + height + ") = " + str(bmi))
print(int(bmi))