from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

df = pd.read_csv("students_data.csv")


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


def get_scores(ids):
    ID1 = ids[0]
    scores = []
    for ID2 in ids[:]:
        scores.append(cosine_similarity_score(ID1, ID2, df))
    combined = list(zip(ids, scores))
    sorted_combined = sorted(combined, key=lambda x: x[1])
    sorted_ids = [item[0] for item in sorted_combined][::-1]
    sorted_scores = [item[1] for item in sorted_combined][::-1]
    return sorted_ids, sorted_scores


@app.route('/get_ids_scores', methods=['POST'])
def add_one():
    ids = request.json.get('ids')  # Get the list of IDs from the request JSON
    if ids is None:
        return jsonify({'error': 'No IDs provided'}), 400
    ids, scores = get_scores(ids)
    return jsonify({'ids': ids, 'scores': scores})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)  # Run on localhost, port 8080
