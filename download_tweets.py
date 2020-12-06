#!/usr/bin/env python

# Resources:
# https://nealcaren.org/lessons/twint/
# https://github.com/twintproject/
# Pulling favorites is unfortunately broken unless you have the user id
#
#

import os,sys
import twint

class UserLikes:
    def __init__(self, username):
        self.username = username
        self.usr_twint_obj = self.configure_twint(username)

        return

    def configure_twint(self, username):
        twint_obj = twint.Config()

        # Temp: Workaround to get the user_id
        twint_obj.Search = f"from:{username}"
        # twint_obj.Store_object = True
        twint_obj.Limit = 100

        # usr_id = twint.output.tweets_list[0].user_id

        # twint_obj.Username = username
        # twint_obj.Limit = 100 # temporary for testing
        twint_obj.Store_csv = True
        # twint_obj.User_id = usr_id

        #Create csv
        usr_csv = open(f"./downloaded_tweets/{username}_tweets.csv", "w+")
        usr_csv.write('status_id, _discard1, tweet_timestamp, tweet_date, tweet_time, username, display_name, '
                      'tweet, _d1,_d2,_d3,_d4,_d5,_d6,_d7,_d8, tweet_url') #Writing header
        twint_obj.Output = f"./downloaded_tweets/{username}_tweets.csv"

        #TODO: Dump that into a db instead of holding it as a csv locally

        return twint_obj

    def download_user_likes(self):
        print(f"Downloading tweets for {self.username}")
        twint.run.Search(self.usr_twint_obj)
        # twint.run.Favorites(self.usr_twint_obj)

        return


def cli_download_seq():

    print("\n\n\n Whose likes are we attempting to download? \n")
    twitter_username = input("Twitter username: @")

    usr = UserLikes(twitter_username)
    usr.download_user_likes()

    print("Finished downloading.")

    return


def main():
    cli_download_seq()

    continue_r = input("Would you like to download another user's likes? (Y/N)")

    while continue_r == 'Y':
	continue_r = input("Would you like to download another user's likes? (Y/N)")
        cli_download_seq()

    return

if __name__ == '__main__':
    main()
    sys.exit(0)
