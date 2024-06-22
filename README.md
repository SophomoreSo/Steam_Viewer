# CS-338-Group-Project Milestone 1

## Overview
We use MySQL 8.0 as our database management system. The SQL queries directory contains four folders, each designed for different database operations.

### 1. Initial Setup
This folder guides you through importing the dataset into your database.

- Open MySQL and login into 'localhost:127.0.0.1'.
- Drag and drop the SQL file from the 'Initial Setup' folder into the MySQL program.
- Replace `price.csv` and `game.csv` paths with the directories where your CSV files are located.
   - For Windows, backward slash ('\') must be replaced with forward slash ('/') to prevent import error.
- Click `Run` to automatically import the data.
- Right click -> 'Refresh All'

### 2. Advanced Search
This folder contains a single SQL file with two functionalities:

- **Advanced Search**: This query allows for multiple search parameters, including name keyword, minimum price, maximum price, minimum rating, maximum rating, etc. It creates a temporary view table to store large data chunks.
- **Sort By**: This query sorts the results based on one attribute: price, number of ratings, or name (alphabetical order).

Since the advanced search query does not return an output, it is combined with the sort query for better representation.

### 3. Price Display
This folder includes three SQL files with queries for displaying prices. The purpose of each query is self-explanatory based on their filenames.

### 4. Refresh Price
This folder contains a query to update prices using data from the web scraping module. The query fetches the current price, along with the current timestamp and `app_id`, for all games listed in our database.

## How to Test Application
- Python 3.10 is used for the setup.
- This is tested under Windows 11 environment.
- Install the following packages via PIP:
  - `pip install pyqt5`
  - `pip install mysql-connector-python`
  - `pip install beautifulsoup4`
  - `pip install PyQtWebEngine`

Please follow the instructions on how to PIP install here: https://youtu.be/fJKdIf11GcI

- Go to the main directory, and open up the command prompt to type `python main.py`.
- When successfully opened up the application, you can enter the name of the game on the main search tab. You can also set the price requirements and rating requirements by clicking the respective settings button.
- After setting up the search parameters, you will be prompted with the login popup. Simply type in the database password that you have set up.

## Implemented Features
The application currently has three implemented features:

1. **Advanced Search**
   - Press Enter or click the 'search' button to see the results.
   - If any games meet the requirements, they will be displayed in the search result tab.

2. **Sort By Feature**
   - On the top of the search result tab, there is a dropdown menu and a triangle button.
   - Click the dropdown menu and select how you want to sort the results. Currently, there are three attributes (price, ratings, name) to sort by. You can also click the triangle button to list the results in ascending or descending order.

3. **Price History Viewer**
   - Click any item listed in the search tab. At the very bottom, a price chart of the game will be displayed. Hover over any point in the graph to see the time info and associated price.

## Additional Comments
- Web scraping tools are attached inside the 'Scraping Tools' folder.
- The websites used for scraping are 'store.steampowered.com/api' and 'gg.deals'.
