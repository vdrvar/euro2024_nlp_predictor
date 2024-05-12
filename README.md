# Predicting Euro 2024 with Transformers

## Project Overview
The `euro2024_nlp_predictor` is a comprehensive project that leverages advanced Natural Language Processing (NLP) and machine learning techniques to predict the outcomes of UEFA Euro 2024 matches. By analyzing the sentiment and content from prominent football news sources, this project aims to provide insights into team performances and public sentiment.

## Features
- **News Aggregation**: Automated scraping of renowned football news websites.
- **Sentiment Analysis**: Analysis of the sentiment surrounding teams, providing insights into public opinion and media portrayal.
- **Nation Classification**: Identification of the primary nation discussed in each article to tailor sentiment analysis.
- **Interactive Predictions Dashboard**: A Streamlit-based dashboard that presents the predictions and sentiment analysis in an interactive format.
- **Automated Data Pipeline**: From news aggregation to data processing and visualization, all components are automated for ease of use.

## Technology Stack
- **Python**: Core programming language for data collection, processing, and dashboard.
- **Beautiful Soup & Requests**: Tools for efficient web scraping.
- **Hugging Face Transformers**: Library providing pre-trained models for Natural Language Processing (NLP), including text classification, information extraction, question answering, and more.
- **Streamlit**: Framework for creating the interactive dashboard.
- **Pandas**: For data manipulation and analysis.
- **Subprocess**: For managing script execution within the Python environment.


## File Structure
euro2024_nlp_predictor/
├── code/  # Folder containing all executable scripts and notebooks
│   ├── data_collection/  # Scripts for data scraping news articles
│   │   ├── crawl_the_news.py  # Main script for crawling news articles
│   │   ├── crawler.py  # Helper functions for crawling
│   │   └── testing_crawling.ipynb  # Testing and examples notebooks
│   │
│   ├── data_processing/  # Scripts for data processing and analysis
│   │   ├── analyze_sentiment.py  # Script to analyze sentiment of articles
│   │   ├── filter_relevant.py  # Script to filter relevant articles
│   │   ├── classify_nations.py  # Script to classify articles by nation
│   │   └── final_ranking.ipynb  # Notebook for computing the final ranking
│   │
│   └── prediction/  # Scripts for prediction and visualizations
│       └── prediction_app.py  # Streamlit application for interactive prediction
│
├── data/  # Folder containing processed data
│   ├── raw/  # Folder containing raw scraped data
│   ├── filtered_file_paths.txt  # Text file with paths to filtered relevant articles
│   ├── country_file_paths.txt  # Text file with paths to articles classified by country
│   └── sentiment_scores.pkl  # Pickled file containing sentiment analysis scores
│
├── magazines.txt  # Text file listing target magazines and their URLs
├── requirements.txt  # Text file listing project dependencies
└── README.md  # This file (project documentation)

## Installation
Clone the repository and install dependencies:
```
git clone https://github.com/yourusername/euro2024_nlp_predictor.git
cd euro2024_nlp_predictor
pip install -r requirements.txt
```

## Usage
The Euro 2024 NLP Predictor project utilizes a Streamlit dashboard to manage the entire data processing pipeline, from data collection to displaying predictive analytics. Follow these steps to get started:

### Setup and Installation
1. Clone the Repository:
   git clone https://github.com/yourusername/euro2024_nlp_predictor.git
   cd euro2024_nlp_predictor

2. Install Dependencies:
   Ensure you have Python installed, then run:
   pip install -r requirements.txt

### Running the Streamlit Dashboard
3. Start the Dashboard:
   - Navigate to the prediction directory:
     ```
     cd code/prediction
     ```
   - Launch the Streamlit app:
     ```
     streamlit run prediction_app.py
     ```
   - This will open the dashboard in your default web browser, typically at `http://localhost:8501`.

### Interacting with the Dashboard
The dashboard is designed to guide you through the entire workflow:
- Crawl News: Begin by collecting news articles from configured sources.
- Filter Relevant Articles: Automatically filter out irrelevant content based on predefined criteria.
- Classify Nations: Classify news articles by the relevant nation for further analysis.
- Analyze Sentiment: Perform sentiment analysis on the classified articles to gauge public sentiment and perceptions.
- Run All Processes: Alternatively, you can use this button to execute all scripts sequentially and see the entire pipeline in action.
- Calculate Winning Probabilities: After running the analysis, view the calculated probabilities for each nation's chances of winning based on sentiment scores.

## Contribution
Contributions to the euro2024_nlp_predictor project are welcome! If you have suggestions for improvements or new features, please follow these steps:
- Fork the repository: Create a fork of this repository on GitHub.
- Make your changes: Implement your changes and enhancements in your forked version.
- Submit a Pull Request: Create a pull request against the original repository with a clear list of what you've done and why it's beneficial to the project.

## License
This project is released under the MIT License - see the LICENSE file for details.
