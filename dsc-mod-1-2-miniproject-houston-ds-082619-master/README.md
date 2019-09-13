
# Module 2 Summative Lab

## Introduction

For today's mini-project, we're going to work on a single big lab to apply what we've learned in Modules 1 & 2!

![](https://media.tenor.com/images/faa7904870d4661b3f077f1c49fbbb46/tenor.gif)

## About This Lab

A quick note before getting started--this lab isn't like other labs you seen so far. This lab is meant to take a good amount of time to complete, so it's much longer and more challenging that the average labs you've seen so far. If you feel like this lab is challenging or that you might be struggling a bit, don't fret--that's by design! With everything we've learned about Web Scraping and APIs, the best way to test our knowledge is to build something substantial! 

## The Project

In this lab, we're going to make use of everything we've learned about APIs and Object-Oriented Programming to extract and transform some data from a SQL database. 

You'll find a database containing information about soccer teams and the matches they've played in the file `database.sqlite`. For this project, our goal is to get the data we think is important from this SQL database, then do some calculations and data transformation. 

Let's get into the specifics of this project.

### The Goal

Start by examining the data dictionary for the SQL database we'll be working with, which comes from this [kaggle page](https://www.kaggle.com/laudanum/footballdelphi). Familiarize yourself with the tables it contains, and what each column means. We'll be using this database to get data on each soccer team and calculate some summary statistics. 

Upon completion of this lab, each unique team in this dataset should have a table containing the following information:

* The name of the team
* The total number of goals scored by the team during the 2011 season
* The total number of wins the team earned during the 2011 season
* A histogram visualization of the team's wins and losses for the 2011 season (store the visualization directly by assigning it to a variable)
* The team's win percentage on days where it was raining during games in the 2011 season. 

![](https://media.giphy.com/media/4TkcwHdT1LSLw2rrEN/giphy.gif)

#### Getting the Weather Data

Note that for this last calculation, you'll need to figure out if it was raining or not during the game. The database itself does not contain this information, but it does contain the date on which the game was played. For this, you'll need to use the [DarkSky API](https://darksky.net/dev) to get the historical weather data for that day. Note that each game is played in a different location, and this information is not contained in our SQL database. However, the teams in this database are largely German, so go ahead and just use the weather in Berlin, Germany as a proxy for this information. If it was raining in Berlin on the day the game was played, count that as rain game--**_you do not need to try and figure out the actual weather at each game's location, because we don't have that information!_**

#### NOTE: The DarkSky API is limited to 1000 free API calls a day, so be sure to test your model on very small samples. Otherwise, you'll hit the rate limit!

## Project Architecture

Unlike previous labs, this lab is more open-ended, and will require you to make design decisions and plan out your strategy for building a system with this many working parts. However, **_using Object-Oriented Programming is a requirement for this project--you must create at least 1 well structured class in your solution!_** Although it may seem easier to "just start coding", this is a classic beginner's mistake. Instead, think about separating out the different functionalities you'll need to reach your goal, and then build classes to handle each. For instance, at minimum, you'll need to:

* Query the SQL database
* Calculate summary statistics
* Get the weather data from the DarkSky API

We **_strongly recommend_** you consider creating separate classes for handling at least some of these of these tasks.  Be sure to plan the **inputs**, **outputs**, and **methods** for each class before you begin coding! 

**_NOTE:_** We have provided some empty class examples below. You are welcome to use a different architecture for this project if you so choose.  You do not have to use each of them, they are just there to give you an idea of what sorts of classes you may want to consider using.

### Rapid Prototyping and Refactoring

It's totally okay to try to get a task working without using OOP. For instance, when experimenting with the DarkSky API for getting historical weather data, it makes sense to just write the code in the cells and rapidly iterate until you get it all working. However, once you get it working, you're not done--you should then **_refactor_** your code into functions or classes to make your code more modular, reusable, understandable, and maintainable! 

In short--do what you need to do to get each separate piece of functionality working, and then refactor it into a class after you've figured it out!

### Some Final Advice

![](https://media2.giphy.com/media/11F0d3IVhQbreE/giphy.gif)

If you haven't built anything this big or complex thus far, you may not yet fully realize how much trial and error goes into it. If your code keeps breaking, resist the urge to get frustrated -- just keep working. Software development is an iterative process!  No one writes perfect code that works just right the first time. You're going to run into _a lot_ of small errors in this project, right up until the point where it just works, and then you're done! However, you can reduce these errors by planning out your code, and thinking about how all of the pieces fit together *before* you begin coding. Once you have some basic understanding of how it all will work, then you'll know what you need to build, and then all that is left is to build it!

ALSO! This is a mini project, meant to take just one day. You may run out of time, and that's okay! But do make sure you've outlined your plan to create classes and tackle the four goals of this project (preferably before you dive in and start coding), and make sure to comment your code *while you're writing it* in case you don't have time to go back later.

DOUBLE ALSO: It's okay to use external tools to make your life easier -- that's what they're for! Using tools like the [DB Browser for SQLite](https://sqlitebrowser.org/) to visualize and interact with your SQL database, or [Postman](https://www.getpostman.com/) to test your API query, is one aspect of working smarter (not harder)! 

In short:

* Plan ahead--you'll thank yourself later!
* Errors and broken code aren't bad, they're normal. 
* Keep working, and stay confident--you can do this!

Good luck--we look forward to seeing your completed project!


```python
# You don't have to use these classes, but here are some example ways you could divide these classes:
class SQLHandler():
    pass
```


```python
class GameDataHandler():
    pass
```

```python
class WeatherHandler():
    pass
```

