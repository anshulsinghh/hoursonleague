<div align="center">⌛ Hours on League</div>
## Background
Hours on League is a script which allows a user to check the amount of hours that a summoner has spent playing League of Legends within the last week. The program asks for the user to input a summoner name (a League of Legends username), it then prints the number of hours that the user spent playing League of Legends within the last 7 days. It prints a message advising the user on how to improve productivity, and then fun facts regarding the amount of League games that they played within the last week. The script aims to help users improve their productivity, as each game of League is around 30 minutes - and the game can be quite addicting.

A sample output of the script is below. I ran it with my own summoner name (robbib):
```
> python3 script.py
Enter a Summoner Name: robbib
Making call: https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/robbib
Making call: https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/TLLXeUnoyHbj0WkN5xT4SK6GCKaYG0rJrNFmihveHmuGiKI?beginIndex=0&endIndex=100
Making call: https://ddragon.leagueoflegends.com/realms/na.json
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3230701666
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3230609466
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3229730442
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3229509936
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3229461269
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3228642180
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3228581586
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3228492258
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3228256571
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3227972456
Making call: https://na1.api.riotgames.com/lol/match/v4/matches/3227670574

You have spent 5.0 hours and 30.0 minutes playing 11 matches of league in the last 7 days.

🙂  Looks like you have been pretty productive last week. You might want to limit your hours for next week to increase productivity even more!

In the time you spent on league, here's some things you could have done:
- Flown from LA to NYC 1.0 times
- Read The Great Gatsby 2.0 times
- Watched Avengers: Endgame 1.0 times
```

## How it Works
"Hours on League takes in a username and then accesses the Riot Games API (Riot Games owns League of Legends) through a package called Cassiopeia. Cassiopeia makes it easy to set up the API, and enables Hours on League to access the individual summoner and their match history. Hours on League then traverses the match history to find the amount of league played within the last week, and prints out the time spent on league, a message on what to improve, and fun facts about how much league was played by the given summoner.

## File Structure
- `script.py` - This is the main script for Hours on League
- `module.py` - This contains important functions that are used by the main script
- `test_functions.py` - This file contains tests for some functions in the module file

## Required Libraries
This project uses the following packages:
- Cassiopeia (used to access the Riot Games API)
- Datetime (used for time calculations)
- Math (used for flooring numbers)
- Arrow (used for time calculations)
- Os (used to exit the script when errors occur)
