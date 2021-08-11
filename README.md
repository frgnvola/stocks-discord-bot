## stocks-discord-bot

## Project Overview
Implement a python bot that keeps a list of your favorite stocks and gives you on demand access to price change analysis via sending commands as messages through Discord.

<img width="731" alt="stockbot_ex" src="https://user-images.githubusercontent.com/88749163/128962754-499a28ec-ccb5-444c-9543-16a6eef204fb.png">

## Libraries used in this project

#### Pandas and Pandas_ta libraries
- Needed for data manipulation and storage in DataFrame classes, Pandas_ta has technical analysis specific functions that make appending useful data to dataframes very easy 
- [Learn more about the pandas library](https://pandas.pydata.org/docs/)
- [Learn more about the pandas_ta library](https://github.com/twopirllc/pandas-ta)

#### yfinance library
- Reliable, threaded, and Pythonic way to download historical market data from Yahoo! finance
- [Learn more about the yfinance library](https://pypi.org/project/yfinance/)

#### Commands library from discord.ext 
- Used to create the discord bot, override defualt commands, and create our own
- [Learn more about the discord commands library](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html)

#### random module 
- Used to create pseudorandom numbers for random greetings list used by bot (completely optional, but fun)
- [Learn more about the Random library](https://docs.python.org/3/library/random.html)

#### datetime module
- Used to automatically update data window 
- [Learn more about the datetime module](https://docs.python.org/3/library/datetime.html)



