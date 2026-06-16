import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_data.csv")

plt.scatter(data["StudyHours"], data["FinalMarks"])

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.show()