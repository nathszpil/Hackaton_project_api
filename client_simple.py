import requests


def main():
    url = 'http://16.171.41.176:8080/get_ids_scores'  # URL of the Flask server
    ids = list(range(5, 145))  # Example list of IDs

    response = requests.post(url, json={'ids': ids})

    if response.status_code == 200:
        ids = response.json().get('ids')
        scores = response.json().get('scores')
        print("ids:", ids)
        print("Scores:", scores)
    else:
        print("Failed to add one to IDs")


if __name__ == '__main__':
    main()
