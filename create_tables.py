#!/usr/bin/env python

from db_management import create_table

#These are the only headers I'm interested in capturing right now

scraped_twitter_schema = """
status_id INT PRIMARY KEY NOT NULL, 
tweet_timestamp TIMESTAMP NOT NULL,
tweet_date TIMESTAMP PRIMARY KEY NOT NULL,
tweet_time TIMESTAMP NOT NULL,
username VARCHAR NOT NULL,
display_name VARCHAR NOT NULL,
tweet VARCHAR(300) NOT NULL,
tweet_url VARCHAR(100) NOT NULL
"""

create_table(table="scraped_tweets", schema=scraped_twitter_schema)