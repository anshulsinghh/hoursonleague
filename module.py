from math import floor
import datetime
import arrow
import os
import cassiopeia as cass # Used to communicate with the Riot Games API

def setup_cassiopeia(api_key, region="NA"):
  """
  Sets up Cassiopeia with a given api_key and region

  Parameters
  ----------
  api_key : string
    The API key that will be used by Cassiopeia to communicate with the Riot 
    Games API
  
  region : string (defaults to "NA" - North America)
    The region that will be used by Cassiopeia when searching for a given user.
    Cassiopeia can only search for a user in the region where their account was
    created. For example when searching for a user in North America, cassiopeia
    must be set up with the "NA" region.

  Returns
  -------
  Nothing is printed if there are no errors setting up Cassiopeia to 
  communicate with the Riot API.

  If the provided region is not valid, a list of all the supported regions will
  be printed and the program will exit.
  """

  cass.set_riot_api_key(api_key) # Set the api key for cassiopeia to use
  
  try:
    # Try to set the region of cassiopeia to our provided region
    cass.set_default_region(region)

  except:
    # Catch errors when the region is not valid, and print the valid list of 
    # supported regions
    print("Region was not valid. Please enter a valid region from the list", 
          "below:")
    region_list = ["NA", "BR", "EUNE", "LAN", "LAS", "OCE", "RU", "TR", "JP", 
                   "PH", "SG", "TW", "VN", "TH", "KR", "CN", "PBE"]

    # Cycle through the region list and print each region with a dash in front
    for region in region_list:
      print("-", region)

    #Exit the program, since there was error
    os._exit(1)


def get_summoner_match_history(name):
  """
  Given a summoner username, get_summoner_match_history tries finding that user
  and returns that user's match history if they exist.

  Parameters
  ----------
  name : string
    The summoner username that cassiopeia will search for, and return their
    match history.

  Returns
  -------
  The match history of the given summoner if everything was successful.

  If the Riot API Key is invalid, an error message will be printed and the
  program will exit.

  If the summoner could not be found, an error message will be printed and the
  program will exit.
  """

  try:
    # Try to retrieve the provided username
    summoner = cass.get_summoner(name=name)

    # Try to retrieve the summoner's match history, then return it 
    match_history = summoner.match_history
    return match_history
  
  except cass.datastores.riotapi.common.APIRequestError:
    # Catch the API Request Error, which occurs when the API key is invalid
    print("The Riot API Key is not valid. Please enter a valid API key.")
    os._exit(1) # Exit the program
  
  except:
    # Any other exception will occur when the summoner cannot be found
    error_message = "The summoner '" + name + "' could not be found." + \
                    "Please enter a valid username."
    print(error_message)
    os._exit(1) #Exit the program


def get_time_last_week():
  """
  Returns
  -------
  Using the arrow time library, get_time_last_week returns the exact time
  from 1 week ago.
  """
  current_time = arrow.utcnow() # Get the current UTC Time
  return current_time.shift(weeks=-1) # Return the shifted time by -1 weeks


def get_last_week_game_data(match_history):
  """
  Given a summoner's match history, get_last_week_game_data returns the total
  duration of matches that occured within the last week.

  Parameters
  ----------
  match_history : MatchHistory
    The given match history that will be parsed to find the total hours and
    minutes of league played this week.

  Returns
  -------
  A list with index 0 being the total duration spent playing league, and index
  1 being the number of matches that were played in the last week.
  """

  # Get the of exactly 1 week ago, this will be used to find all the matches
  # that were played within the last week.
  last_week_time = get_time_last_week()

  # This will store the total duration of all matches played within the last
  # week.
  total_duration = datetime.timedelta()

  num_matches = 0 # The number of matches played in the last week

  # Loop through all of the matches in the given match history
  for match in match_history:
    # Check if the match occurred within the last week. If it's creation time
    # is greater than the time of exactly 7 days ago, we know that it occurred
    # within this last week.
    if match.creation >= last_week_time:
      total_duration += match.duration # Increment the total time
      num_matches += 1 #Increment the number of matches played in the last

    else:
      # Matches in the match history are organized chronologically, so we can
      # break from the for loop the instant a match is found that did not
      # occur within the last week.
      break

  return [total_duration, num_matches]


def get_hours_and_minutes(time):
  """
  Given a TimeDelta object, time, get_hours_and_minutes reformats the object
  into hours and minutes and returns this as an integer list.

  Parameters
  ----------
  time : TimeDelta
    The given time that will be broken down into hours and minutes.

  Returns
  -------
  A list with index 0 being the hours of the timedelta object, and index 1
  being the minutes of the timedelta object.
  """

  # Get the total seconds of the time object
  totalseconds = time.total_seconds()
  
  # Find the total hours in the time object
  totalhours = totalseconds//3600
  # Find the total minutes in the time object
  totalminutes = (totalseconds%3600) // 60 

  # Return a list composing of the total hours and minutes
  return [totalhours,totalminutes] 


def get_analysis(num_hours):
  """
  Given the number of hours, minutes, and matches played within the last week,
  get_analysis returns a custom message which lets users know how productive
  they have been within the last week, and how they can improve their
  productivity.

  Parameters
  ----------
  num_hours : int
    Number of hours of league that were played in the last week

  Returns
  -------
  A custom string message that lets users know how they can improve their
  gaming habits to boost productivity.
  """

  # These are all different strings that will get returned based on how well
  # the user performed last week (in terms of hours played)
  did_well = '\n😁  Great Job! Looks like you have been really' + \
             ' productive last week.'
  did_alright = '\n🙂  Looks like you have been pretty productive last ' + \
                'week. You might want to limit your hours for next week to' + \
                ' increase productivity even more!'
  did_poorly = '\n😦  Seems like you play a lot! Definitely try limiting ' + \
               'your hours to be more productive.'
  did_horrible = '\n😡  You should really limit your hours, you probably' + \
                 ' cannot get much work done if you play this much.'

  # Depending on how many hours are played, a different analysis string 
  # is returned
  if num_hours <= 1:
    return did_well
  elif num_hours > 1 and num_hours <= 5:
    return did_alright
  elif num_hours > 5 and num_hours <= 10:
    return did_poorly
  else:
    return did_horrible


def print_fun_facts(num_hours, num_minutes):
  """
  Given the number of hours and minutes of league played within the last week,
  print_fun_facts prints out fun facts regarding the amount of league that a
  summoner has played within the last week. Specifically, print_fun_facts shows
  how many times a summoner could have flown from LA to NYC, how many times 
  they could have read the Great Gatsby, and how many times they could have 
  watched Avengers: Endgame if they had not played league in the last week.

  Parameters
  ----------
  num_hours : int
    Number of hours of league that were played in the last week
  num_minutes : int
    Number of minutes of league that were played in the last week
  """

  # If the number of hours are less than 1, there are no real analytics that
  # can be given to the user, so the program exits
  if num_hours < 1:
    os._exit(1)

  print("\nIn the time you spent on league, here's some things you", 
        "could have done:")

  # Get the total number of minutes that the user spent playing league in the
  # last week
  total_mins = num_hours * 60 + num_minutes

  # Number of hours it takes to fly coast to coast
  hours_to_fly_from_la_to_nyc = 5

  # Find how far or how many times the user could have flown coast to coast
  flying_data = time_to_perform_task(total_mins, hours_to_fly_from_la_to_nyc)

  # Check if the data returned is not a whole number, but a percentage
  # This will occur if hte user hasn't played enough league to complete more
  # than 1 flight from coast to coast
  if flying_data[0]:
    print("- Flown ", flying_data[1],"% of the way from LA to NYC", sep='')
  else:
    print("- Flown from LA to NYC", flying_data[1], "times")

  # Repeating the same process, but with the Great Gatsby
  hours_to_read_great_gatsby = 2.62
  gatsby_data = time_to_perform_task(total_mins, hours_to_read_great_gatsby)
  if gatsby_data[0]:
    print("- Read ", gatsby_data[1],"% of The Great Gatsby", sep='')
  else:
    print("- Read The Great Gatsby ", gatsby_data[1], " times", sep='')
  
  # Again repeating the same process to print analytics about Avengers: Endgame
  hours_to_watch_endgame = 3.2
  endgame_data = time_to_perform_task(total_mins, hours_to_watch_endgame)
  if endgame_data[0]:
    print("- Watched ", endgame_data[1],"% of Avengers: Endgame", sep='')
  else:
    print("- Watched Avengers: Endgame ", endgame_data[1], " times", sep='')


def time_to_perform_task(total_mins, total_hours_for_task):
  """
  time_to_perform_task is a supporting function for the print_fun_facts 
  function above. It takes in the total minutes spent playing league in the 
  last week, and the amount of hours required to perform a task. Given these 
  two parameters, time_to_perform_task will return a list. Index 0 is a boolean 
  which tells whether or not the following number at Index 1 is a percentage or
  not. Index 1 will either be a percentage if 
  total_mins < total_hours_for_task * 60 or it will be a whole number if 
  total_mins >= total_hours_for_task*60. In essence it will be a percentage if 
  there was not enough time played to complete one iteration of the task, 
  and a whole number if the user could have completed the task multiple times 
  over.

  Parameters
  ----------
  total_mins : int
    Number of hours of league that were played in the last week
  total_hours_for_task : int
    Number of hours required for a sepcific task

  Returns
  -------
  A list with index 0 being a boolean which tells if the number at inde 1 is a
  percentage or not. 
  """

  # Get the number of mins for the task
  num_mins_for_task = total_hours_for_task * 60 

  # Find the percentage of the task that is completed
  percent_done = total_mins / num_mins_for_task
  percent_done *= 100

  is_percent = False # Holds if the number is a percentage
  if percent_done < 100:
    is_percent = True # The second number will be a percentage
    return [is_percent, floor(percent_done)]
  
  # Change the second nubmer to be the number of times the task can be 
  # completed
  times_done = percent_done // 100
  return [is_percent, times_done]