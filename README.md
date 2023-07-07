# Movie Recommendation System

This project is a movie recommendation system built using Streamlit. It suggests movies to users based on their preferences and utilizes content-based filtering techniques.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributing](#contributing)

## Introduction
The Movie Recommendation System is a web application designed to help users discover new movies that match their interests. It utilizes content-based filtering to analyze user preferences and generate personalized movie recommendations.

## Features
- Movie search functionality
- Personalized movie recommendations
- Display of movie posters and titles
- User-friendly interface

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/AbhiramDaka/MovieRecommendationSystem.git
   ```
2. Install the required dependencies:
   ```
   pip install streamlit
   ```
3. create pickle files.
   ```
   pip install streamlit
   pickle.dump(movies, open('movies_list.pkl', 'wb'))  #Refer movierecommend.ipynb file
   pickle.dump(similarity, open('similarity.pkl', 'wb'))
   ```
4. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage
1. Open the web browser and access the application at `http://localhost:8501`.
2. Select a movie from the dropdown list.
3. Click the "Search" button to get movie recommendations based on the selected movie.
4. View the recommended movies with their respective posters and titles.

## Data
The project uses a movie dataset that includes movie titles, IDs, and other relevant information. The dataset is used to generate recommendations based on user preferences.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request with a description of your changes.


## Images
![image](https://github.com/AbhiramDaka/MovieRecommendationSystem/assets/94378828/c30d3e6e-3be3-42ae-be4c-2680680f18e1)
