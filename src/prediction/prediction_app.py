import streamlit as st
import subprocess
import os
import threading
import pickle
import pandas as pd

def run_script(script_path):
    """Utility function to run a script and stream the output with head and tail shown if too long."""
    os.chdir(os.path.dirname(script_path))
    process = subprocess.Popen(['python', '-u', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    st.write(f"Running {os.path.basename(script_path)}... Please check the output below:")
    output_container = st.empty()
    all_output = []
    max_lines = 20  # Set maximum number of lines to keep in memory

    for line in iter(process.stdout.readline, ''):
        if line:
            all_output.append(line)
            if len(all_output) > max_lines:
                all_output = all_output[:10] + ["...\n", "... (skipping lines) ...\n", "... \n"] + all_output[-10:]
            output_container.code(''.join(all_output))

    process.stdout.close()
    error_output = process.stderr.read()
    if error_output:
        st.error("Errors encountered during processing:")
        st.code(error_output)
    process.stderr.close()

    process.wait()
    return_code = process.returncode
    if return_code == 0:
        st.success(f"{os.path.basename(script_path)} completed successfully.")
    else:
        st.error(f"{os.path.basename(script_path)} process exited with code {return_code}.")

def run_all_scripts():
    scripts = [
        '../data_collection/crawl_the_news.py',
        '../data_processing/filter_relevant.py',
        '../data_processing/classify_nations.py',
        '../data_processing/analyze_sentiment.py'
    ]
    for script in scripts:
        run_script(script)

def process_sentiment_scores():
    file_path = "../../data/sentiment_scores.pkl"
    with open(file_path, 'rb') as file:
        sentiment_scores = pickle.load(file)

    min_score = min(sentiment_scores.values())
    adjustment = abs(min_score) if min_score < 0 else 0
    epsilon = 0.01

    for key in sentiment_scores:
        sentiment_scores[key] += adjustment + epsilon

    total_score = sum(sentiment_scores.values())
    for key in sentiment_scores:
        sentiment_scores[key] /= total_score

    sorted_sentiment_scores = {k: v for k, v in sorted(sentiment_scores.items(), key=lambda item: item[1], reverse=True)}
    percentage_scores = {k: v * 100 for k, v in sorted_sentiment_scores.items()}
    
    st.markdown("### Percentage Chance of Winning Based on Sentiment Analysis")
    df = pd.DataFrame(list(percentage_scores.items()), columns=['Nation', 'Chance'])
    st.bar_chart(df.set_index('Nation')['Chance'])

    # Optionally, show the data in a nicer table format
    st.table(df.assign(Chance=df['Chance'].apply(lambda x: f"{x:.2f}%")))

st.title('Euro 2024 Transformer Predictor')

if st.button('Crawl News'):
    crawl_script_path = '../data_collection/crawl_the_news.py'
    run_script(crawl_script_path)

if st.button('Filter Relevant Articles'):
    filter_script_path = '../data_processing/filter_relevant.py'
    run_script(filter_script_path)

if st.button('Classify Nations'):
    classify_nations_script_path = '../data_processing/classify_nations.py'
    run_script(classify_nations_script_path)

if st.button('Analyze Sentiment'):
    analyze_sentiment_script_path = '../data_processing/analyze_sentiment.py'
    run_script(analyze_sentiment_script_path)

if st.button('Run All Processes'):
    threading.Thread(target=run_all_scripts, daemon=True).start()

if st.button('Calculate Winning Probabilities'):
    process_sentiment_scores()
