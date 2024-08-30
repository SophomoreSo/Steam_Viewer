# Steam Viewer

## Overview
We use MySQL 8.0 as our database management system. The SQL queries directory contains four folders, each designed for different database operations.

### 1. Initial Setup
This folder guides you through importing the dataset into your database.


<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/1.png" height=150px>
</div>


- Open MySQL and login into `localhost:127.0.0.1`.


<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/2.png" height=150px>
</div>


- Drag and drop the SQL file from the 'Initial Setup' folder into the MySQL program.


<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/3.png" height=150px>
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/4.png" height=150px>
</div>

- Replace `price.csv` and `game.csv` paths with the directories where your CSV files are located.
   
   - For Windows, backward slash ('\\') must be replaced with forward slash ('/') to prevent import error.



<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/5.png" height=150px>
</div>


- Click `Run` to automatically import the data.


<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/6.png" height=150px>
</div>


- Right click -> `Refresh All`


<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/Database_Setup/7.png" height=150px>
</div>


- Double check that steamdb schema is selected.

### 2. Advanced Search
This folder contains a single SQL file with two functionalities:

- **Advanced Search**: This query allows for multiple search parameters, including name keyword, minimum price, maximum price, minimum rating, maximum rating, etc. It creates a temporary view table to store large data chunks.
- **Sort By**: This query sorts the results based on one attribute: price, number of ratings, or name (alphabetical order).

Since the advanced search query does not return an output, it is combined with the sort query for better representation.

### 3. Price Display
This folder includes three SQL files with queries for displaying prices. The purpose of each query is self-explanatory based on their filenames.

### 4. Refresh Price
This folder contains a query to update prices using data from the web scraping module. The query fetches the current price, along with the current timestamp and `app_id`, for all games listed in our database.

### 5. Steam Review

This folder contains queries that output a list of reviews made by Steam users. 
The query will return game reviews associated with the provided `app_id`.
The table is divided into two parts for performance optimization:
  1. Game_Discussion(discussion_id, game_id)
  2. Discussion(discussion_id, user_id, voted_up, review_text, timestamp_created)
<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/SQL queries/5_Steam_Review/Performance Tuning Proof.png">
</div>
There are two SQL files in this folder: one optimized for performance and the other not. Please run both queries to compare their runtime.

### 6. Find Streamer

These SQL queries outputs a list of streamers associated with the `app_id` that has a past experience in playing the game.
The query takes one parameter `app_id` and outputs streamer's channel name and the number of followers of the channel.
The table is also divided into two parts for optimization:
  1. Streamer_App(app_id, streamer_id)
  2. Streamer(streamer_id, streamer_name, followers)
<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/SQL queries/6_Find_Streamer/Performance Tuning Proof.png">
</div>
Again, run both queries for comparison.

## How to Test Application
- Python 3.10 is used for the setup.
- This is tested under Windows 11 environment.
- Install the following packages via PIP:
```
  pip install pyqt5
  pip install mysql-connector-python
  pip install beautifulsoup4
  pip install PyQtWebEngine
```
Please follow the instructions on how to PIP install here: https://youtu.be/fJKdIf11GcI
- Go to the main directory, and open up the command prompt to type `python main.py`.

<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/2.png" height=150px>
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/3.png" height=150px>
</div>


- When successfully opened up the application, you can enter the name of the game on the main search tab. You can also set the price requirements and rating requirements by clicking the respective settings button.

<div align="left">
   <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/4.png" height=150px>
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/5.png" height=150px>
</div>
- After setting up the search parameters, you will be prompted with the login popup. Simply type in the database password that you have set up.

## Implemented Features
The application currently has three implemented features:


<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/6.png" height=200px>
</div>



1. **Advanced Search**
   - Press Enter or click the 'search' button to see the results.
   - If any games meet the requirements, they will be displayed in the search result tab.
  


<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/8.png" height=200px>
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/9.png" height=200px>
</div>


2. **Sort By Feature**
   - On the top of the search result tab, there is a dropdown menu and a triangle button.
   - Click the dropdown menu and select how you want to sort the results. Currently, there are three attributes (price, ratings, name) to sort by. You can also click the triangle button to list the results in ascending or descending order.

<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/10.png" height=200px>
</div>


<div align="left">
<img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/11.png" height=400px>
</div>

3. **Price History Viewer**
   - Click any item listed in the search tab. At the bottom, a price chart of the game will be displayed. Hover over any point in the graph to see the time info and associated price.

<div align="left">
  <img src="https://github.com/SophomoreSo/Steam_Viewer/blob/main/img/App_Test/12.png" height=400px>
</div>

4. **Steam Reviews**
   - Scroll to the very bottom of the game page, reviews and comments about the game is displayed.

## Additional Comments
- Web scraping tools are attached inside the 'Scraping Tools' folder.
- The websites used for scraping are 'store.steampowered.com/api' and 'gg.deals'.


