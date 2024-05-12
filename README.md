# Euro 2024 NLP Predictor

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
│
├── code/ # All executable scripts and notebooks
│ ├── data_collection/ # Scripts for data scraping
│ │ ├── crawl_the_news.py # Main script for news crawling
│ │ ├── crawler.py # Helper functions for crawling
│ │ └── testing_crawling.ipynb # Testing and examples
│ │
│ ├── data_processing/ # Scripts for data processing and analysis
│ │ ├── analyze_sentiment.py # Sentiment analysis script
│ │ ├── filter_relevant.py # Filter relevant articles
│ │ ├── classify_nations.py # Classify articles by nation
│ │ └── final_ranking.ipynb # Notebook for final ranking computation
│ │
│ └── prediction/ # Prediction and visualization scripts
│ └── prediction_app.py # Streamlit dashboard application
│
├── data/ # Stored data from the crawlers and analyses
│ ├── raw/ # Raw scraped data
│ ├── filtered_file_paths.txt # Paths to filtered relevant articles
│ ├── country_file_paths.txt # Classified articles by country
│ └── sentiment_scores.pkl # Output from sentiment analysis
│
├── magazines.txt # List of target magazines and URLs
├── requirements.txt # Project dependencies
└── README.md # Project README file

## Installation
Clone the repository and install dependencies:
```
git clone https://github.com/yourusername/euro2024_nlp_predictor.git
cd euro2024_nlp_predictor
pip install -r requirements.txt
```

## Usage
To run the full pipeline from data collection to prediction display:

Start the data collection: Run crawl_the_news.py from the data_collection directory.
Process the collected data: Execute scripts in data_processing to filter and analyze data.
View predictions: Launch prediction_app.py from the prediction directory to view the interactive dashboard.
Contribution
Contributions are welcome! Please fork the repository and submit pull requests with your proposed changes.

License
This project is released under the MIT License - see the LICENSE file for details.
