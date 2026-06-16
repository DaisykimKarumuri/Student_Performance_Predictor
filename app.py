from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    study = float(request.form['study'])
    attendance = float(request.form['attendance'])
    previous = float(request.form['previous'])
    assignment = float(request.form['assignment'])

    result = model.predict(
        [[study, attendance, previous, assignment]]
    )

    marks = round(result[0], 2)

    if marks >= 90:
        category = "Excellent"
        remark = "Keep up the excellent work!"
    elif marks >= 75:
        category = "Good"
        remark = "Focus on assignments and practice tests to improve further."
    elif marks >= 50:
        category = "Average"
        remark= "Increase study hours and attendance for better performance."
    else:
        category = "Needs Improvement"
        remark = "Follow a regular study schedule and seek guidance from teachers."
        
    return render_template(
    'index.html',
    prediction=marks,
    category=category,
    remark=remark,
    study=study,
    attendance=attendance,
    previous=previous,
    assignment=assignment
)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)