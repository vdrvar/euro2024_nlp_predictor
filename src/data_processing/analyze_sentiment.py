import pickle
import random
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import time

# Load the tokenizer and model from Hugging Face
model_name = "MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

def calculate_sentiment_score(text):
    candidate_labels = ["positive sentiment", "negative sentiment"]
    results = classifier(text, candidate_labels, multi_label=False)
    probabilities = {label: score for label, score in zip(results['labels'], results['scores'])}
    sentiment_score = probabilities.get('positive sentiment', 0) - probabilities.get('negative sentiment', 0)
    return sentiment_score

# Load the dictionary mapping countries to file paths
dict_file_path = "../../data/country_file_paths.txt"
with open(dict_file_path, 'rb') as file:
    nation_mapped_files = pickle.load(file)

def analyze_nation_articles(nation_files):
    sentiment_scores = {}
    total_start_time = time.time()  # Start timing the entire process

    for nation, files in nation_files.items():
        scores = []
        for file_path in files:
            print(f"Processing {file_path}...")
            file_start_time = time.time()  # Start timing for this file

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                score = calculate_sentiment_score(text)
                scores.append(score)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

            file_end_time = time.time()  # End timing for this file
            print(f"Processed {file_path} in {file_end_time - file_start_time:.2f} seconds.")

        # Add random noise to prevent ties and compute the average sentiment
        noise = random.uniform(-0.01, 0.01)  # Small noise to prevent exact ties
        sentiment_scores[nation] = sum(scores) / len(scores) + noise if scores else noise

    total_end_time = time.time()  # End timing the entire process
    print(f"Total sentiment analysis completed in {total_end_time - total_start_time:.2f} seconds.")
    return sentiment_scores

# Calculate sentiment scores for each nation
sentiment_scores = analyze_nation_articles(nation_mapped_files)

# Save the sentiment scores to a new dictionary file
scores_file_path = "../../data/sentiment_scores.pkl"
with open(scores_file_path, 'wb') as file:
    pickle.dump(sentiment_scores, file)

print("Sentiment scores saved to:", scores_file_path)
