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
  ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/18e6bc57-42f4-469e-9fd9-953e76d4a807)
- Filter Relevant Articles: Automatically filter out irrelevant content based on predefined criteria.
   ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/3cd2a3d6-3437-44f1-91db-ab969b33a858)
- Classify Nations: Classify news articles by the relevant nation for further analysis.
 ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/6ed5ed91-8641-4810-a945-aec20042bf1e)
- Analyze Sentiment: Perform sentiment analysis on the classified articles to gauge public sentiment and perceptions.
  ![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/a626dcd0-0d71-4cd7-b6c2-29b34114f161)
- Run All Processes: Alternatively, you can use this button to execute all scripts sequentially and see the entire pipeline in action.
- Calculate Winning Probabilities: After running the analysis, view the calculated probabilities for each nation's chances of winning based on sentiment scores.
![image](https://github.com/vdrvar/euro2024_nlp_predictor/assets/48907543/e38abdb3-d7af-47e8-bb99-47b31f071eb0)


```
Percentage scores loaded successfully:
Italy: 8.98%
Portugal: 8.58%
Belgium: 7.92%
Türkiye: 7.13%
Croatia: 6.40%
Germany: 5.10%
Hungary: 5.09%
France: 4.93%
Georgia: 3.72%
Switzerland: 3.63%
Netherlands: 3.45%
Spain: 3.43%
Czechia: 3.38%
Austria: 3.33%
Albania: 3.33%
Romania: 3.27%
Slovakia: 3.26%
Ukraine: 3.19%
Poland: 3.19%
Scotland: 3.19%
Serbia: 3.18%
Denmark: 1.72%
Slovenia: 0.46%
England: 0.13%
```

## Project Conclusion

The euro2024_nlp_predictor project demonstrates the potential of using NLP and machine learning to analyze football news and predict public sentiment for UEFA Euro 2024. The interactive dashboard and sentiment analysis provide valuable insights, but the project is limited by the small transformer model used, necessary for running on a single CPU. Stronger results could be achieved with more powerful infrastructure, such as advanced transformer models requiring GPU acceleration.


## Contribution
Contributions to the euro2024_nlp_predictor project are welcome! If you have suggestions for improvements or new features, please follow these steps:
- Fork the repository: Create a fork of this repository on GitHub.
- Make your changes: Implement your changes and enhancements in your forked version.
- Submit a Pull Request: Create a pull request against the original repository with a clear list of what you've done and why it's beneficial to the project.

## License
This project is released under the MIT License - see the LICENSE file for details.
