import pandas as pd

df = pd.read_csv("students_data.csv")

weights = {
    'Student Age': 2,
    'Sex': 2,
    'Graduated high-school type': 1,
    'Additional work': 3,
    'Regular artistic or sports activity': 2,
    'Weekly study hours': 3,
    'Reading frequency (non-scientific books/journals)': 1,
    'Reading frequency (scientific books/journals)': 1,
    'Attendance to classes': 3,
    'Preparation to exams with': 3,
    'Preparation to exams when': 3,
    'Taking notes in classes': 1,
    'Listening in classes': 2,
    'Discussion improves my interest and success in the course': 3
}


def get_matching_score(ID1, ID2, weights, df):
    matching_score = 0

    for key in weights:
        if df.loc[df['STUDENT ID'] == ID1, key].iloc[0] == df.loc[df['STUDENT ID'] == ID2, key].iloc[0]:
            matching_score += weights[key]
    return matching_score

for i in range(1,146):
    for j in range(1,146):
        print(f"matching score  between {i} and {j} = {get_matching_score(i,j,weights,df)}")