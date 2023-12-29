h=float(input("Enter height in metres"))
w=float(input("Enter weight in kgs"))
bmi=round((w/(h*h)),1)
if(bmi>=30.0):
    print("Obese")
elif(bmi>=25.5):
    print("Overweight")
elif(bmi>=18.5):
    print("Normal")
else:
    print("Underwight")
