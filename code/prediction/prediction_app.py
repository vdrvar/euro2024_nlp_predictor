import streamlit as st
import subprocess
import os
import pandas as pd
import pickle

def run_script_and_display_output(script_path):
    """Execute a script and display its output in Streamlit."""
    st.write(f"Running {os.path.basename(script_path)}...")
    output_container = st.empty()
    all_output = []

    os.chdir(os.path.dirname(script_path))
    process = subprocess.Popen(['python', '-u', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

    for line in iter(process.stdout.readline, ''):
        if line:
            all_output.append(line)
            display_output = ''.join(all_output[-20:])  # Display the last 20 lines
            output_container.code(display_output)

    process.stdout.close()
    error_output = process.stderr.read()
    if error_output:
        st.error("Errors encountered during processing:")
        st.code(error_output)
    process.stderr.close()

    return_code = process.wait()
    if return_code == 0:
        st.success(f"{os.path.basename(script_path)} completed successfully.")
    else:
        st.error(f"{os.path.basename(script_path)} process exited with code {return_code}.")

def run_all_scripts():
    """Run all designated scripts sequentially."""
    scripts = [
        '../data_collection/crawl_the_news.py',
        '../data_processing/filter_relevant.py',
        '../data_processing/classify_nations.py',
        '../data_processing/analyze_sentiment.py'
    ]
    for script in scripts:
        run_script_and_display_output(script)

def process_sentiment_scores():
    """Process and display sentiment scores."""
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
    st.table(df.assign(Chance=df['Chance'].apply(lambda x: f"{x:.2f}%")))

    # Save the percentage_scores to a file
    output_path = "../../data/percentage_scores.pkl"
    with open(output_path, 'wb') as output_file:
        pickle.dump(percentage_scores, output_file)

    st.success(f"Percentage scores saved successfully to {output_path}")

st.title('Euro 2024 Transformer Predictor')

if st.button('Crawl News'):
    run_script_and_display_output('../data_collection/crawl_the_news.py')

if st.button('Filter Relevant Articles'):
    run_script_and_display_output('../data_processing/filter_relevant.py')

if st.button('Classify Nations'):
    run_script_and_display_output('../data_processing/classify_nations.py')

if st.button('Analyze Sentiment'):
    run_script_and_display_output('../data_processing/analyze_sentiment.py')

if st.button('Run All Processes'):
    run_all_scripts()

if st.button('Calculate Winning Probabilities'):
    process_sentiment_scores()
