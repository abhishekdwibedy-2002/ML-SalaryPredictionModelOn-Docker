# Loading dataset
import pandas as pd
dataset = pd.read_csv("Salary_Data.csv")
print("Dataset has been loaded ...")

# features 
x = dataset["YearsExperience"]
# selection
y = dataset["Salary"]   

x = x.values
x = x.reshape(30,1) #changing the datatype from pandas to numpy

#loading linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y) #training the model
print("Model has been created ...")


# Our model has been trained now we have to save it 
import joblib
joblib.dump(model,"salarypredictor_model.pk1")

print("MODEL SAVED SUCCESSFULLY IN WORKSPACE ...")

