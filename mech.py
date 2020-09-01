# mech.py is actually the backend portion of this entire application.
# It does all the retrieving of data from the user given input.
# First:
#   It imports json library and get_close_matches
#   module from the difflab library. The json library
#   is used to load the data.json file and the difflab’
#   get_close_matches function is used to fetch relative
#   data of the provided user input in case the user misspelled.

import json
from difflib import get_close_matches

# second:
#   Then it creates an instance of the json data set and names it data.

data = json.load(open("data.json"))


# Third:
#  Now we create a function called translate that takes
#  a single string as an input and uses that input as a
#  key to retrieve corresponding values of the key from
#  the data dictionary. The function also checks if the
#  provided input is misspelled of not and tries to recommend
#  possible solution.
def translate(w):
    w = w.lower()  # ignores the case type
    l = []
    # fetches the meaning if its in the database
    if w in data:
        return data[w]  # returns it
    # if it doesnt exists then finds the nearest key possible and asks for correction.
    elif len(get_close_matches(w, data.keys())) > 0:
        l.append("Did you mean {} instead?".format(get_close_matches(w, data.keys())[0]))
    # if it doesnt match any key in any way then informs the user that its not in the current dictionary
    else:
        l.append("The word doesn't exist. Please double check it.")
    # returns the retrieved lists of meanings for the given key
    return l
