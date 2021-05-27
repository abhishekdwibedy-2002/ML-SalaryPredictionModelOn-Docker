import joblib

model = joblib.load('salarypredictor_model.pk1')
x = float(input("Enter Years of Experience(in decimal): "))
result = int(model.predict([[x]]))
print("Salary will be :",  result) 
