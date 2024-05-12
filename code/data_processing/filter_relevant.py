from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import os
import time

# Load the tokenizer and model from Hugging Face
model_name = "MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

def classify_text(text, candidate_labels):
    # Use the pipeline for zero-shot classification
    results = classifier(text, candidate_labels, multi_label=False)
    # Organize results into a dictionary where each label is mapped to its corresponding score
    return {label: score for label, score in zip(results['labels'], results['scores'])}

def filter_files(file_paths, relevant_label="relevant football article including at least one national team"):
    print("Filtering for relevant football articles...")
    relevant_files = []
    candidate_labels = ["relevant football article including at least one national team", "irrelevant content"]

    for file_path in file_paths:
        file_start_time = time.time()  # Start timing for this file
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            results = classify_text(text, candidate_labels)
            if results[relevant_label] > 0.5:  # Adjust the threshold as needed
                relevant_files.append(file_path)
            file_end_time = time.time()  # End timing for this file
            print(f"Processed {file_path} in {file_end_time - file_start_time:.2f} seconds.")
        except Exception as e:
            print(f"An error of type {type(e).__name__} occurred while filtering: {str(e)}")

    return relevant_files

def get_all_file_paths(directory):
    file_paths = []  # List to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

# Main process with overall timing
def main():
    start_time = time.time()  # Start timing the entire process

    directory_path = '../../data/raw'
    all_file_paths = get_all_file_paths(directory_path)

    # Filter the files
    filtered_files = filter_files(all_file_paths)

    # Write filtered files to a file
    file_path = "../../data/filtered_file_paths.txt"
    with open(file_path, "w") as file:
        for item in filtered_files:
            file.write("%s\n" % item)

    end_time = time.time()  # End timing the entire process
    print(f"Total filtering completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
