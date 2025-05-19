
import pandas as pd
import numpy as np
import pickle

#Importing the file as df
df = pd.read_csv('diabetes.csv')

#Renaming the DiabitiesPedigreeFunction to DPF
df = df.rename(columns={'DiabitiesPedigreeFunction':'DPF'})

#Copy the df as df_copy
df_copy=df.copy(deep=True)

#copying all the attributes of the Dataset and also replacing 0 with NaN
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']]=df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

#removing null and 0 values in the Data set
#df_copy['Pregnancies'].fillna(df_copy['Pregnancies'].mean() ,inplace=True)
df_copy['Glucose'].fillna(df_copy['Glucose'].mean() ,inplace=True)
df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean() ,inplace=True)
df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].mean(), inplace=True)
df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace=True)
df_copy['BMI'].fillna(df_copy['BMI'].median() ,inplace=True)

#Defining Train Set and Training sets
from sklearn.model_selection import train_test_split
X = df.drop(columns='Outcome')
y = df['Outcome']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)

# Importing Random Forest Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train,y_train)

filename='diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier,open(filename, 'wb'))

