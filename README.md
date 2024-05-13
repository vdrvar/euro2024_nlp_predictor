# Predicting Euro 2024 with Transformers

## Project Overview
The `euro2024_nlp_predictor` is a comprehensive project that leverages advanced Natural Language Processing (NLP) and machine learning techniques to analyze football news from prominent magazines and predict public sentiment for UEFA Euro 2024. This project aims to provide insights into team performances and public sentiment by scraping and analyzing content from key sports magazines, including:

1. **L'Équipe (France)** - More than just a sports newspaper, L'Équipe is essential for daily sports news in France, with a strong focus on football.
2. **FourFourTwo (United Kingdom)** - A global football magazine known for its comprehensive coverage, including in-depth features and tactical analysis.
3. **Kicker (Germany)** - A staple in German sports journalism, Kicker extensively covers both domestic and international football.
4. **La Gazzetta dello Sport (Italy)** - Italy's leading sports daily, renowned for its thorough focus on Serie A and international football.
5. **Marca (Spain)** - A major Spanish sports newspaper known for its detailed coverage of La Liga and Spanish football.

By extracting and analyzing data from these sources, the project provides a detailed view of the evolving dynamics in football as the Euro 2024 approaches.


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


## Usage
The Euro 2024 NLP Predictor project utilizes a Streamlit dashboard to manage the entire data processing pipeline, from data collection to displaying predictive analytics. Follow these steps to get started:

### Setup and Installation
1. Clone the Repository:
   ```
   git clone https://github.com/yourusername/euro2024_nlp_predictor.git
   cd euro2024_nlp_predictor
   ```

2. Install Dependencies:
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

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
     ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/4c5c7cc4-4ccb-491a-9dce-977a861ff7cd)


### Interacting with the Dashboard
The dashboard is designed to guide you through the entire workflow:
- Crawl News: Begin by collecting news articles from configured sources.
- Filter Relevant Articles: Automatically filter out irrelevant content based on predefined criteria.
- Classify Nations: Classify news articles by the relevant nation for further analysis.
- Analyze Sentiment: Perform sentiment analysis on the classified articles to gauge public sentiment and perceptions.
- Run All Processes: Alternatively, you can use this button to execute all scripts sequentially and see the entire pipeline in action.
  ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/ef3d9932-7638-4022-b7ce-3b2a31ed3dd6)

- Calculate Winning Probabilities: After running the analysis, view the calculated probabilities for each nation's chances of winning based on sentiment scores.

## Contribution
Contributions to the euro2024_nlp_predictor project are welcome! If you have suggestions for improvements or new features, please follow these steps:
- Fork the repository: Create a fork of this repository on GitHub.
- Make your changes: Implement your changes and enhancements in your forked version.
- Submit a Pull Request: Create a pull request against the original repository with a clear list of what you've done and why it's beneficial to the project.

## License
This project is released under the MIT License - see the LICENSE file for details.
