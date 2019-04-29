# SI-206---Final-Project
Final Project By: Sydney Bruce, Dylan Rabin, and William Zhang

Files Included:
    Keys.py
    YelpAPI.py
        YelpCalc.sqlite
    ZomatoAPI.py
        ZomatoCalc.sqlite
    OpenWeatherMap.py
    WeatherCalculations.py
    CombinedDatabase.sqlite

How it Works:
    import requests
    import json
    import Keys
    import sqlite3
    import matplotlib
    import matplotlib.pyplot as plt

Begin by running all the main python files for each API:
    YelpAPI.py
    ZomatoAPI.py
    OpenWeatherMap.py

After running the above, it will create a combined database (CombinedDatabase.sqlite) that includes three tables, one for each API. Each table will contain 100 items from each API, 10 individual items from each of our selected inputed cities:
    Atlanta, GA
    Boston, MA
    Chicago, IL
    Detroit, MI
    Houston, TX
    Los Angeles, CA
    New York City, NY
    Philadelphia, PA
    San Francisco, CA
    Seattle, WA

The goal is to compare the data from these cities, specifically the hotel ratings and prices, restaurant price range and average rating, and then the weather for May 24th and May 25th.

After the database is populated with all the necessary data the code then completes calculations pulled from the information from the tables in the database. Each python file for each API computes its own calculations and write them to files. NOTE: OpenWeatherMap.py has a seperate python file that completed the calculations, so also run WeatherCalculations.py to complete the WeatherAPI calculations.

Both the Zomato and Yelp API's create a seperate database that contains our calculations:
    YelpCalc.sqlite
    ZomatoCalc.sqlite

This made it easier for us to pull our calculations to create our visualizations. 

Once all the calculations are run we all pull from the database to create our individual visualizations. Each code contains a seperate function to create our visualizations and all of them do pull from the existing databases. 

Results:
Following the instructions above will create multiple visualizations for each API:
    Zomato: 4 visualizations (4 bar charts)
    Weather: 2 visualizations (1 bar chart, 1 scatterplot)
    Yelp: 2 visualizations (2 bar charts)

All are .png files pasted in our final report


Citations: 
    4/10/19
    We decided on which API’s we would use to pull and compare data as we had a problem finding data to compare
    API websites(Zomato, Yelp, and OpenWeatherMap)
    We were able to extract the data from the API and populate databases with the information gathered
    4/15/19
    We needed help created visualizations and used the discussion as a template
    Discussion Slides (plot_final.py)
    We were able to easily gain knowledge on how to properly format our code to create various visualizations
    4/19/19 - 4/22/19
    Needed assistance to correctly access the Yelp API
    Assistance adding rows to a database
    Stack Overflow
    Stack Overflow allowed us to solve all the existing problems and help us move forward with our project.
    4/29/19
    Our team realized that we had not yet added all of our tables into a single database and need advice on how to fix it
    Piazza
    Other groups had similar questions and one question was this exact question so we were able to solve the problem.


