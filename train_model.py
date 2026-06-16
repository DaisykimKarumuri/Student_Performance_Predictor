import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load dataset
data = pd.read_csv("student_data.csv")

# Input and Output
X = data[['StudyHours', 'Attendance',
          'PreviousMarks', 'AssignmentScore']]
y = data['FinalMarks']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", r2_score(y_test, pred))

joblib.dump(model, "model.pkl")
print("Model trained successfully!")