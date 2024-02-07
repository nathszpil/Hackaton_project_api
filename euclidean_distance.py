import numpy as np
import pandas as pd

df = pd.read_csv("students_data.csv")

def euclidean_distance(ID1, ID2, df):
    row1 = df[df['STUDENT ID'] == ID1].iloc[0]
    row2 = df[df['STUDENT ID'] == ID2].iloc[0]

    features1 = row1.drop('STUDENT ID').values
    features2 = row2.drop('STUDENT ID').values

    distance = np.sqrt(np.sum((features1 - features2) ** 2))

    return distance


for i in range(1, 146):
    for j in range(1, 146):
        print(f"Euclidean distance between {i} and {j} = {euclidean_distance(i, j, df)}")