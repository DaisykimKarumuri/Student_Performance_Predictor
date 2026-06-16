import joblib

model = joblib.load("model.pkl")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance: "))
previous_marks = float(input("Previous Marks: "))
assignment_score = float(input("Assignment Score: "))

prediction = model.predict(
    [[study_hours, attendance,
      previous_marks, assignment_score]]
)

print("Predicted Final Marks:", round(prediction[0], 2))