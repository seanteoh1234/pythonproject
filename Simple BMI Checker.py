weight=float(input("What is your weight?"))
height=float(input("What is your height?"))
#insert weight in kg and height in cm.
BMI = weight/((height/100)**2)
if BMI < 18.5:
   print("Underweight")
elif BMI >= 18.5 and BMI < 25 :
   print("Normal")
elif BMI >= 25 and BMI < 30 :
   print ("Overweight")
else :
   print ("Obesity")
