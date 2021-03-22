import csv
import pandas as pd
import plotly.express as px

with open("py2/class1.csv",newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
total_entries = len(file_data)

total_marks = 0

for marks in file_data:
    total_marks = total_marks + float(marks[1])

mean = total_marks/total_entries

print("Mean is : " + str(mean))

df = pd.read_csv("py2/class1.csv")

fig = px.scatter(df, x = "Student Number", y = "Marks")
fig.update_layout(shapes = [dict(type = 'line',y0 = mean, y1 = mean, x0 = 0, x1 = total_entries)])
fig.show()