# This is a script for the third challenge problem
# The problem this investigates is the geolocation of 
# people using the #blacklivesmatter hashtag on Twitter
# before and after the recent shooting in Baton Rouge.
from twython import Twython
import json
import pandas, time
import numpy

# Twitter keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Connect to the Twiter API
twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Find the hashtag #BLM
# Twitter only allows you to grab 100 tweets at a time.
hashtag = '#BLM'
count = 100

tweets=[]

# Loop to collect as many tweets as Twitter will give me
for i in range(0,50):

    # Collect tweets from Sunday night backwards
    if(0 == i):
        try:
            search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-18')
        except error:
            break
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        try:
            search_results = twitter_api.search(q=hashtag,include_entities='true',max_id=next_id, count=count, until='2016-07-18')
        except:
            break

    # Save tweets
    for result in search_results['statuses']:
        tweets.append(result)


    # Extract the last tweet given to reseed the request
    try:
        oldest = search_results['search_metadata']['next_results']
        next_id = oldest.split('max_id=')[1].split('&')[0]
    except:
        break

# Collect tweets with hashtag #blacklivesmatter
hashtag = '#blacklivesmatter'

# Loop to collect as many tweets as Twitter will give me
for i in range(0,50):

    # Collect tweets from Sunday night backwards
    if(0 == i):
        try:
            search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-18')
        except error:
            break
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        try:
            search_results = twitter_api.search(q=hashtag,include_entities='true',max_id=next_id, count=count, until='2016-07-18')
        except:
            break
        
    # Save tweets
    for result in search_results['statuses']:
        tweets.append(result)


    # Extract the last tweet given to reseed the request
    try:
        oldest = search_results['search_metadata']['next_results']
        next_id = oldest.split('max_id=')[1].split('&')[0]
    except:
        break




    
# Collect tweets from before the Baton Rouge incident
# Find the hashtag #BLM
# Twitter only allows you to grab 100 tweets at a time.
hashtag = '#BLM'

# Loop to collect as many tweets as Twitter will give me
for i in range(0,50):

    # Collect tweets from Sunday night backwards
    if(0 == i):
        try:
            search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-17')
        except error:
            break
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        try:
            search_results = twitter_api.search(q=hashtag,include_entities='true',max_id=next_id, count=count, until='2016-07-17')
        except:
            break
        
    # Save tweets
    for result in search_results['statuses']:
        tweets.append(result)


    # Extract the last tweet given to reseed the request
    try:
        oldest = search_results['search_metadata']['next_results']
        next_id = oldest.split('max_id=')[1].split('&')[0]
    except:
        break

# Collect tweets with hashtag #blacklivesmatter
hashtag = '#blacklivesmatter'

# Loop to collect as many tweets as Twitter will give me
for i in range(0,50):

    # Collect tweets from Sunday night backwards
    if(0 == i):
        try:
            search_results = twitter_api.search(q=hashtag, count=count, until='2016-07-17')
        except error:
            break
    else:
        # After the first call we should have max_id from result of previous call. Pass it in query.
        try:
            search_results = twitter_api.search(q=hashtag,include_entities='true',max_id=next_id, count=count, until='2016-07-17')
        except:
            break
        
    # Save tweets
    for result in search_results['statuses']:
        tweets.append(result)


    # Extract the last tweet given to reseed the request
    try:
        oldest = search_results['search_metadata']['next_results']
        next_id = oldest.split('max_id=')[1].split('&')[0]
    except:
        break

# Write out the csv file
m_data = []
log_tweets = './' + 'tweets.csv'
with open(log_tweets,'w') as outfile:
    for line in tweets:
        m_data.append(json.loads(json.dumps(line)))
        outfile.write(json.dumps(line))
        outfile.write("\n")
        
# Convert to a pandas dataframe
tweetdb = pandas.DataFrame()
tweetdb['id'] = list(map(lambda x: x['id'],m_data))
tweetdb['created_at'] = list(map(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(x['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), m_data))
tweetdb['text'] = list(map(lambda x: x['text'].encode('utf-8'), m_data))
tweetdb['user'] = list(map(lambda x: x['user']['screen_name'], m_data))
tweetdb['location'] = list(map(lambda x: x['user']['location'], m_data))
tweetdb['followers'] = list(map(lambda x: x['user']['followers_count'], m_data))
tweetdb['log_followers'] = list(map(lambda x: numpy.log(x['user']['followers_count']), m_data))

header = ["created_at","followers"]
tweetdb.to_csv('output.csv',columns=header)










