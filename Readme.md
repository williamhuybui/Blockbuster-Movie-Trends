![time release](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/theater.jpg)
# Blockbuster Movie Trends

#### -- Project Status: [Completed]

## Project Intro/Objective
The objective of this project is to find the trend of popular movies in the U.S. It answers 5 questions:

### 1) What is the average profit and rating?

![profit rating](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/profit_rating.png)

The average rating is 6.845, ranging from 4.8 (Independent Day) to 8.3 (Inception).

Avengers: Endgame unsurprisingly made more money than any movie in history with $2.4b in profit. The lowest one comes from Dark Phoenix with $45m. The average profit of this top 220 movies is $538m

### 2) Which MPAA rating attracts the most audience?
![Movie type](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/movie_type.png)

Teen friendly movies, PG-13, are top of the chart for the Motion Picture Association of America (MPAA) rating with over 50% of the top-grossing movie market. The reason is simple, it has the widest range of audience.

### 3) When is the best time to release a movie
![time release](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/time_release.png)

The best months for going to the box office are :

**Summer blockbusters:** May, June, July.

**Thanksgiving and Christmas time:**  November, December.

### 4) Best genres to invest

![best genre](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/best_genre.png)

No 1: Action-Adventure such as Wonder Woman, Captain America, The Hunger Games.

No 2: Action-Fantasy such as Lord of the Rings, Maleficent, Star Wars.

No 3: Animation-Family such as Lion King, Inside Out, Wall-E.

### 5) How many good actors should we hire?

![actor](https://github.com/williamhuybui/Blockbuster-Movie-Trends/blob/master/Picture/top_actor.jpg)

We define `good actor` by looking at their rank on IMDb. For each movie, we extract the top 10 casts and check if they are in the top 1000 actors on the list. Some of the people on the list are Jack Nicholson, Leonardo DiCaprio, Morgan Freeman.

The graph shows that action, adventure, and family genres have an average of 5 A-rank actors. Interestingly, history movies have the most, 7 actors on average

## Data
The data come from 220 top gross revenue movies from 2009 to 2019. This is obtained through the API requests from the [movies database](https://www.themoviedb.org/). Also, a list of the 1000 best actor is collected from IMDb.

## Technologies
* Python library: `Pandas`, , SQL by `sqlite3`.
* Visualization: `Tableau`
* Scrapping: `bs4` and `API request`

## Get started

1) Create the file `api_key.py`
2) Read [this](https://www.themoviedb.org/faq/api) to know how to create an `API key`
3) After obtaining the key, go to `api_key.py`, type `key = `Your API key` `
4) Run the `DataCollention notebook`

## Link to Presentation
* [Blog](https://dev.to/williamhuybui/blockbuster-movie-trends-h94)

## Contact
* Email: williamhuybui@gmail.com
