# Program 15: Decision Tree classifier
# Requires: pip install scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Features: [hours studied, attendance percentage]
X = [[1,40],[2,50],[2,60],[3,65],[4,70],[5,80],[6,90],[7,95]]
y = ["Fail","Fail","Fail","Pass","Pass","Pass","Pass","Pass"]
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
hours = float(input("Hours studied: "))
attendance = float(input("Attendance percentage: "))
print("Predicted result:", model.predict([[hours, attendance]])[0])
