import pickle

# Load the sentiment scores from a pickle file
file_path = "../../data/sentiment_scores.pkl"
with open(file_path, 'rb') as file:
    sentiment_scores = pickle.load(file)

# Determine the smallest adjustment needed to make all scores positive
min_score = min(sentiment_scores.values())
adjustment = abs(min_score) if min_score < 0 else 0

# Small constant to ensure no zero probabilities
epsilon = 0.01

# Adjust scores and add a small constant
for key in sentiment_scores:
    sentiment_scores[key] = sentiment_scores[key] + adjustment + epsilon

# Normalize the scores to sum to 1 (convert to probabilities)
total_score = sum(sentiment_scores.values())
for key in sentiment_scores:
    sentiment_scores[key] = sentiment_scores[key] / total_score

# Sort the dictionary by values in descending order
sorted_sentiment_scores = {k: v for k, v in sorted(sentiment_scores.items(), key=lambda item: item[1], reverse=True)}

# Optionally, to display the percentage chance of winning
percentage_scores = {k: v * 100 for k, v in sorted_sentiment_scores.items()}

return percentage_scores