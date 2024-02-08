import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = pd.read_csv("students_data.csv")
weights = {
    'Student Age': 2,
    'Sex': 2,
    'Graduated high-school type': 1,
    'Additional work': 100,
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

def cosine_similarity_score(ID1, ID2, df):
    # Locate the rows corresponding to ID1 and ID2
    row1 = df[df['STUDENT ID'] == ID1].iloc[0]
    row2 = df[df['STUDENT ID'] == ID2].iloc[0]

    # Extract feature vectors from the rows
    features1 = row1.drop('STUDENT ID').values.reshape(1, -1)
    features2 = row2.drop('STUDENT ID').values.reshape(1, -1)

    # Calculate cosine similarity
    score = cosine_similarity(features1, features2)[0][0]

    return score

def weighted_cosine_similarity_score(ID1, ID2, df, weights):
    # Locate the rows corresponding to ID1 and ID2
    row1 = df[df['STUDENT ID'] == ID1].iloc[0]
    row2 = df[df['STUDENT ID'] == ID2].iloc[0]

    # Extract feature vectors from the rows
    features1 = row1.drop('STUDENT ID').values
    features2 = row2.drop('STUDENT ID').values

    # Apply weights to the feature vectors
    weighted_features1 = features1 * np.array([weights.get(col, 1) for col in df.columns if col != 'STUDENT ID'])
    weighted_features2 = features2 * np.array([weights.get(col, 1) for col in df.columns if col != 'STUDENT ID'])

    # Calculate cosine similarity
    score = cosine_similarity(weighted_features1.reshape(1, -1), weighted_features2.reshape(1, -1))[0][0]

    return score


print('score with 146 : ', cosine_similarity_score(1, 146, df))
print('score with 147 : ', cosine_similarity_score(1, 147, df))

print('w score with 146 : ', weighted_cosine_similarity_score(1, 146, df, weights))
print('wscore with 147 : ', weighted_cosine_similarity_score(1, 147, df, weights))



