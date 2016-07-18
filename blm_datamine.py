# This is a script for the third challenge problem
# The problem this investigates is the geolocation of 
# people using the #blacklivesmatter hashtag on Twitter
# before and after the recent shooting in Baton Rouge.
from twython import Twython
import json

# Twitter keys
CONSUMER_KEY = 'szzIqYXh0j4KsYiLcBfltVSEx'
CONSUMER_SECRET = 'yO3h76bky5fKxfFUI4zb0KEejxEEVDrKaBmOMsd0rM3HbhcKzk'
OAUTH_TOKEN = '18917349-kkp3XQ4uszMObYURy2AVrsVDf06KR6fZOgRdALpEF'
OAUTH_TOKEN_SECRET = 'jlZvzVsTsYdigqVY7lGNlnDjDoBqOEGzr2quuStbMmhAF'

# Connect to the twiter API
twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


hashtag = '#BLM'
count = 100

search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-18')
tweets = search_results['statuses']

for i in range(0,100):


    #----------------------------------------------------------------#
    # STEP 1: Query Twitter
    # STEP 2: Save the returned tweets
    # STEP 3: Get the next max_id
    #----------------------------------------------------------------#

    # STEP 1: Query Twitter
    if(0 == i):
        # Query twitter for data. 
        search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-18')
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        search_results = twitter_api.search(q=hashtag,include_entities='true',max_id=next_max_id, count=count, until='2016-07-18')

    # STEP 2: Save the returned tweets
    for result in search_results['statuses']:
        tweets.append(result)


    # STEP 3: Get the next max_id
    try:
        # Parse the data returned to get max_id to be passed in consequent call.
        next_results_url_params = search_results['search_metadata']['next_results']
        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        # No more next pages
        break

# Show one sample search result by slicing the list...
#print(json.dumps(statuses[0], indent=1))