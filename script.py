import module

# Your Riot API Key
api_key = "RGAPI-1eb6369c-833d-4608-959b-ef9a6d8e5193"

# Setting up Cassiopeia with Riot API Key and API Region
module.setup_cassiopeia(api_key)

# Ask the user to input a summoner to retrieve the number of hours they've 
# spent on league in the last week
summoner_name = input("Enter a Summoner Name: ")

# Retrieve the Summoner's match history
match_history = module.get_summoner_match_history(summoner_name)

# Retrieve all games played within the last week
last_week_data = module.get_last_week_game_data(match_history)
total_duration = last_week_data[0]
num_matches = last_week_data[1]

# Parse the total hours and minutes spent playing league in the last week
total_hours_and_minutes = module.get_hours_and_minutes(total_duration)
total_hours = total_hours_and_minutes[0]
total_minutes = total_hours_and_minutes[1]

# Print out the number of hours, minutes, and matches of league that the 
# summoner played in the last week.
print("\nYou have spent", total_hours, "hours and", total_minutes, 
      "minutes playing", num_matches, "matches of league in the last 7 days.")

# Get and print out analytics based on the number of hours spent on league
analysis = module.get_analysis(total_hours)
print(analysis)

# Print out fun facts based on the total hours and minutes played this week
module.print_fun_facts(total_hours, total_minutes)