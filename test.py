ids = [1, 3, 2, 5, 4]
scores = [20, 50, 30, 10, 40]

# Combine ids and scores into tuples
combined = list(zip(ids, scores))

# Sort the combined list based on scores
sorted_combined = sorted(combined, key=lambda x: x[1])
sorted_ids = [item[0] for item in sorted_combined]
sorted_scores = [item[1] for item in sorted_combined]

print("Sorted IDs:", sorted_ids)
print("Sorted Scores:", sorted_scores)