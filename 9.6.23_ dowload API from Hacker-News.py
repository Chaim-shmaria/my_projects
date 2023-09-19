import requests
import csv
from tqdm import tqdm

# this is a python script that scrapes the "hacker-news" website, retrives all
# the info of all the top stories in the site, and saves it to a CSV file.

# constants
PATH = "hacker-news-info.csv"
HN_PREFIX = 'https://hacker-news.firebaseio.com/v0/'
HN_TOP_STORIES_SUFFIX = 'topstories.json?print=pretty'
HN_SINGLE_ID_SUFFIX = 'item/{}.json?print=pretty'  # reuse suffix for all item

# First: creates a shortcut to the link to the 'top' list. Second: Creates a loop that will take all the items in the
# list and download its required details. For this loop we will need a link that is only useful that feeds all the
# identities to the details.

# send HTTP request to get all the top stories ID's and save the request
response = requests.get(HN_PREFIX + HN_TOP_STORIES_SUFFIX)
if response.status_code != 200:   # something that wrong
    raise ConnectionError

# save the ID's in a list
list_of_id = response.json()

# initialize on empty list ready to store all the dictionaries
# that hld the info of all the top stories
list_of_info_dicts = []

list_of_id = list_of_id[:3]  # used for test if it works

# add all dict's to array
for single_id in tqdm(list_of_id):
    # save the info of the story at the ID, as a dict
    single_story_info = requests.get(HN_PREFIX + HN_SINGLE_ID_SUFFIX.format(single_id))

    if single_story_info.status_code != 200:
        continue

    # save the info in the response in a dict
    single_story_info_dict = single_story_info.json()
    # add the dict to the list of dict's
    list_of_info_dicts.append(single_story_info_dict)

# create list of all possible keys
keys = set()  # initialize on empty set
# iterate over dicts list
for info_dicts in list_of_info_dicts:
    keys.update(info_dicts)

# for row in list_of_info_dicts:
#     print(row)

# save the data in a CSV file
with open(PATH, "w") as file:
    writer = csv.DictWriter(file, fieldnames=list(keys))
    # write column headers
    writer.writeheader()
    writer.writerows(list_of_info_dicts)
