# Movie Data Collection and Analysis

## Topic Overview

This project retrieves and processes data from the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to collect information about popular movies.
<br>By using the TMDb API, this script fetches movie data across multiple pages, aggregates it, and stores it in a Pandas DataFrame for easy analysis and manipulation. 

 ## Description

The script makes requests to the TMDb API to fetch details of popular movies. It retrieves data for **10k** movies across multiple pages, extracting the following fields:

- **Title**: The name of the movie.
- **Release Date**: The date the movie was released.
- **Popularity**: A popularity score assigned to the movie.
- **Vote Average**: The average vote score for the movie.
- **Original Language**: The language the movie was originally produced in.
- **Overview**: A brief description of the movie.


The data can be used for a variety of purposes, such as trend analysis, recommendations, or exploring patterns in the movie industry.

## How to Clone this Project

To clone this repository to your local machine and start working with the project, follow these steps:

1. **Install Git**: Make sure that you have Git installed on your local machine. If not, you can download and install it from [here](https://git-scm.com/downloads).

2. **Clone the Repository**:
   Open your terminal (or Git Bash) and run the following command:

   ```bash
   git clone https://github.com/rabin20-04/Movies-Data-Collection-from-API.git
   ```
