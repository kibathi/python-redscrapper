import praw
# import pandas as pd
# import datetime as dt #only if you want to analyze the date created feature

reddit = praw.Reddit(client_id='LtLc7nl1tFkkNA', 
                     client_secret='JjAS3uiVQTFLFE384Wa8wz5OeKTP2A', 
                     user_agent='praw1', 
                     username='kibben01', 
                     password='vulcan01')

subreddit = reddit.subreddit('python')
hot_python = subreddit.hot()
hot_python = subreddit.hot(limit=3)
for submission in hot_python:
    if not submission.stickied:
        # print(submission.title)
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           submission.ups,
                                                                            submission.downs,
                                                                           submission.visited))
subreddit.unsubscribe()                                        
         

