# 🎬 Movie Recommendation System

This project is a web-based application that provides movie recommendations based on a selected movie. It utilizes a machine learning model to compute similarity between movies and recommends similar ones. The application is built using Streamlit for the frontend and uses The Movie Database (TMDB) API to fetch movie posters.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Movie Selection**: Select a movie you like from a dropdown list.
- **Recommendation Display**: Get a list of recommended movies similar to the selected movie.
- **Poster Display**: View posters of the recommended movies fetched using the TMDB API.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd movie-recommendation-system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have the following files in your project directory:
    - `Movies.pkl`: Contains the movie data.
    - `Classifier.pkl`: Contains the similarity matrix.

5. Obtain an API key from [The Movie Database (TMDB)](https://www.themoviedb.org/documentation/api) and replace `YOUR_API_KEY` in the code with your actual API key.

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

2. The web application will open in your default web browser.

3. Select a movie from the dropdown menu to see recommendations.

## Dependencies

- `streamlit`: Used for creating the web application.
- `pandas`: Used for data manipulation and analysis.
- `requests`: Used for making HTTP requests to fetch movie posters.
- `pickle`: Used for loading the pre-trained model and movie data.

You can install all dependencies using:

```bash
pip install -r requirements.txt

```
## 🔗 Follow us
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kothapalli-santhoshi-368951254/)

## Feedback
If you have any feedback, please reach out to us at santhu2002.kothapalli@gmail.com