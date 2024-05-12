from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import os
import time
import pickle

# Load the tokenizer and model from Hugging Face
model_name = "MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

def classify_nation(text, candidate_labels):
    results = classifier(text, candidate_labels, multi_label=False)
    if results and 'labels' in results and 'scores' in results:
        sorted_results = sorted(zip(results['labels'], results['scores']), key=lambda x: x[1], reverse=True)
        most_relevant_label = sorted_results[0][0]
        return most_relevant_label
    return None

def map_files_to_nations(file_paths, nations):
    nation_files = {nation: [] for nation in nations}
    for file_path in file_paths:
        print(f"Classifying {file_path}...")
        file_start_time = time.time()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            nation = classify_nation(text, nations)
            if nation:
                nation_files[nation].append(file_path)
            file_end_time = time.time()
            print(f"Processed {file_path} in {file_end_time - file_start_time:.2f} seconds.")
        except Exception as e:
            print(f"An error occurred while reading file {file_path}: {e}")
    return nation_files

def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

def main():
    start_time = time.time()
    nations = ["Germany", "Scotland", "Hungary", "Switzerland", "Spain", "Croatia", "Italy", "Albania",
               "Slovenia", "Denmark", "Serbia", "England", "Poland", "Netherlands", "Austria", "France",
               "Belgium", "Slovakia", "Romania", "Ukraine", "Türkiye", "Georgia", "Portugal", "Czechia"]

    file_path = "../../data/filtered_file_paths.txt"
    with open(file_path, 'r') as file:
        filtered_files = [line.strip() for line in file.readlines()]

    nation_mapped_files = map_files_to_nations(filtered_files, nations)
    print("Files mapped to nations:")
    for nation, files in nation_mapped_files.items():
        print(f"{nation}: {len(files)} files")

    dict_file_path = "../../data/country_file_paths.txt"
    with open(dict_file_path, 'wb') as file:
        pickle.dump(nation_mapped_files, file)
    print("Dictionary saved to:", dict_file_path)

    end_time = time.time()
    print(f"Total operation completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
