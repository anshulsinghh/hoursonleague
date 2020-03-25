from datetime import timedelta
from module import get_analysis, get_hours_and_minutes\

"""
This function tests the get_analysis function in the module file
"""
def test_get_analysis():
  assert callable(get_analysis) # Check if the function is callable
  
  # Check that for inputs from 0 to 14, that the output is a string
  for i in range(0, 15):
    assert isinstance(get_analysis(i), str)

  # These strings are used to test if the outputs of the function are correct
  did_well = '\n😁  Great Job! Looks like you have been really' + \
             ' productive last week.'
  did_alright = '\n🙂  Looks like you have been pretty productive last ' + \
                'week. You might want to limit your hours for next week to' + \
                ' increase productivity even more!'
  did_poorly = '\n😦  Seems like you play a lot! Definitely try limiting ' + \
               'your hours to be more productive.'
  did_horrible = '\n😡  You should really limit your hours, you probably' + \
                 ' cannot get much work done if you play this much.'

  # For any input less than 2, the string did_well should be returned
  for i in range (-20, 2):
    assert get_analysis(i) == did_well

  # For any input >= 2 and < 6, the string did_alright should be returned
  for i in range(2, 6):
    assert get_analysis(i) == did_alright

  # For any input >= 6 and < 11, the string did_poorly should be returned
  for i in range(6, 11):
    assert get_analysis(i) == did_poorly
  
  # For any input >= 11 and < 20, the string did_horrible should be returned
  for i in range(11, 20):
    assert get_analysis(i) == did_horrible

  # Test that the proper values are still returned with floating point values
  assert get_analysis(1.2) == did_alright
  assert get_analysis(10.2) == did_horrible
  assert get_analysis(8.2) == did_poorly

"""
This function tests the get_hours_and_minutes function in the module file
"""
def test_get_hours_and_minutes():
  assert callable(get_hours_and_minutes) # CHeck if the function is callable

  # Loop through hours from -100 to 99
  for hours in range(-100, 100):
    # Loop through minutes from 0 to 59 (if minutes = 60 it will wrap around to
    # be a new hour)
    for minutes in range(0, 60):
      # Create a new timedelta object
      delta = timedelta(hours=hours, minutes=minutes)

      #Check that the hours and minutes match
      assert get_hours_and_minutes(delta) == [hours, minutes]

      #Check that the value returned is a list
      assert isinstance(get_hours_and_minutes(delta), list)