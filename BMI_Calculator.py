print ("Welcome to BMI calculator")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height*height)
bmi = round(bmi,2)

if bmi <= 18.5 :
  print (f"your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi <= 25 :
  print (f"your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi <= 30:
  print (f"your BMI is {bmi}, you are slightly overweight.")
elif 30 < bmi <= 35:
  print (f"your BMI is {bmi}, you are obese.")
else :
  print (f"your BMI is {bmi}, you are clinically obese.")