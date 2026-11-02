import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


students = ["Arun", "Priya", "Ravi", "Meena", "Karthik",
            "Divya", "Suresh", "Kavya", "Sanjay", "Anitha"]

attendance = [95, 88, 76, 92, 85, 98, 80, 89, 72, 94]

python_marks = [85, 92, 78, 88, 75, 95, 80, 90, 68, 87]
sql_marks = [78, 88, 82, 90, 70, 92, 85, 86, 65, 89]
pandas_marks = [90, 95, 80, 85, 72, 96, 88, 91, 70, 84]
excel_marks = [88, 90, 75, 92, 80, 94, 82, 87, 73, 91]
powerbi_marks = [82, 94, 85, 87, 78, 90, 86, 93, 67, 88]

print("Students:", students)
print("Attendance (%):", attendance)
print("Python Marks:", python_marks)
print("SQL Marks:", sql_marks)
print("Pandas Marks:", pandas_marks)
print("Excel Marks:", excel_marks)
print("Power BI Marks:", powerbi_marks)
# total_marks for each students
total_marks=[]
print("Average marks for all students: ")
for i in range(len(students)):
    total=[python_marks[i] + sql_marks[i] + pandas_marks[i] + excel_marks[i] + powerbi_marks[i]]
    total_marks.append(total)
    average= (python_marks[i] + sql_marks[i] + pandas_marks[i] + excel_marks[i] + powerbi_marks[i])/5
    
    print(students[i]," : ",average)

print("Total_marks: ",total_marks)

for i in range(len(students)):
    if (python_marks[i] >=35 and sql_marks[i] >=35 and pandas_marks[i]>=35 and excel_marks[i] >= 35 and powerbi_marks[i] >=35):
        print(students[i]," : pass")
    else:
        print(students[i]," : Fail")

#Numpy
marks = np.array([python_marks, sql_marks, pandas_marks, excel_marks, powerbi_marks])
print("Marks array:\n", marks)

total_marks=np.sum(marks,axis=0)
print("Total marks for all students: ", total_marks)
average_marks=np.mean(marks,axis=0)
print("Average marks for all students: ", average_marks)
highest_mark = np.max(marks,axis=1)
print("Highest marks in each subject: ", highest_mark)
lowest_mark=np.min(marks,axis=1)
print("Lowest marks in each subject: ", lowest_mark)

average_mark_by_sunject = np.mean(marks,axis=1)
print("Average marks by subject: ", average_mark_by_sunject)

for i in range(len(students)):
    if (average_marks[i] < 50):
        print("student have average below 50: ",students[i])
    else:
        print("student have average above 50: ",students[i])

print("Median marks..")
print("python : ", np.median(python_marks))
print("SQL : ",np.median(sql_marks))
print("Pandas : ",np.median(pandas_marks))
print("Excel : ",np.median(excel_marks))
print("Power BI : ",np.median(powerbi_marks))

print(" Standared Deviation..")
print("python : ", np.std(python_marks))
print("SQL : ",np.std(sql_marks))
print("Pandas : ",np.std(pandas_marks))
print("Excel : ",np.std(excel_marks))
print("Power BI : ",np.std(powerbi_marks))

df =pd.DataFrame({"student_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                  "student_names" : students,
                  "attendance%" : attendance,
                  "python_marks" : python_marks,
                  "sql_marks" : sql_marks,
                  "pandas_marks" : pandas_marks,
                  "excel_marks" : excel_marks,
                  "powerbi_marks" : powerbi_marks
                  })
print(df)
df["Total_marks"] = df["python_marks"] + df["sql_marks"] + df["pandas_marks"] + df["excel_marks"] + df["powerbi_marks"]
df["Average_marks"] = df["Total_marks"]/5
print(df)

print("students who have low attendance : " ,df[df["attendance%"] < 75]["student_names"].tolist())
print("Highest total marks : ",df[df["Total_marks"] == df["Total_marks"].max()]["student_names"].tolist())

df["departments"] = ["CSE", "ECE", "CSE", "MECH", "CSE", "ECE", "MECH", "CSE", "ECE", "MECH"]
print(df.groupby("departments")[["Total_marks"]].mean())
pass_students=[]
fail_students=[]
for i in range(len(students)):
    if (df["python_marks"][i] >=35 and df["sql_marks"][i] >=35 and df["pandas_marks"][i]>=35 and df["excel_marks"][i] >= 35 and df["powerbi_marks"][i] >=35):
        pass_students.append(students[i])
    else:
        fail_students.append(students[i])
print("Pass students: ", pass_students)
print("Fail students: ", fail_students)
df["Result"]= ({"pass" : pass_students, "fail" : fail_students})
print(df.groupby("Result")[["student_names"]].count())
print("Number of pass students : ", len(pass_students))
print("Number of fail students : ", len(fail_students))
print(df)
#  subject with the highest and lowest average marks.
print("Subject with highest average mark : ", df[["python_marks", "sql_marks", "pandas_marks", "excel_marks", "powerbi_marks"]].mean().idxmax())
print("Subject with lowest average mark : ", df[["python_marks", "sql_marks", "pandas_marks", "excel_marks", "powerbi_marks"]].mean().idxmin())
average_mark_by_subject = df[["python_marks", "sql_marks", "pandas_marks", "excel_marks", "powerbi_marks"]].mean()  

print("Students by average marks (descending):")
print(df.sort_values("Average_marks", ascending=False))

print(df[(df["attendance%"] > 90) & (df["Average_marks"] < 30)])

plt.bar(students,average_marks)
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()

plt.hist(marks, bins=5, label=["Python", "SQL", "Pandas", "Excel", "Power BI"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.legend()
plt.show()

plt.pie(total_marks, labels= students)
plt.title("Total Marks Distribution")
plt.show()

subjects = ["Python", "SQL", "Pandas", "Excel", "Power BI"]
plt.plot(subjects, average_mark_by_subject, marker='o')
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Average Marks by Subject")
plt.show()

plt.scatter(attendance, average_marks)
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Average Marks")
plt.show()

# x=range(len(subjects))
# width=0.35
# plt.figure(figsize=(10, 5))
# plt.bar(x, pass_students, width, label="Pass Students")
# plt.bar([i + width for i in x], fail_students, width, label="Fail Students")
# plt.xlabel("Subjects")
# plt.ylabel("Number of Students")
# plt.title("Pass and Fail Students by Subject")
# plt.xticks([i + width/2 for i in x], subjects)
# plt.legend()
# plt.show()

