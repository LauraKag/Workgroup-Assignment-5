# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:55:26 2018

@author: laura
"""

#%%

#In this workgroup exercise we will model a social network like application
#named Tooter. In Tooter, users will be able to create toots, and other users
#following them should be able to see those toots.

#The needed operations you’ll need are:
#• A user can create a toot
#• A user can follow other users
#• A user can unfollow other users
#• A user can see their timeline. Their timeline should contain all their
#own toots + all the toots of all the people they follow.


#You’ll need to create an HTTP server for this assignment. Put it in the
#server module in your repository.

#You’ll also need a http client for this API, put it in the client module.
#Remember that the server and the client will need to communicate using
#JSON.

import requests 

def toot(user,toot):
    response=requests.post("http://127.0.0.1:5000/post_toot/{}/{}".format(user,toot))
    return response.json()

def delete_toot(user,toot):
    response=requests.delete("http://127.0.0.1:5000/delete_toot/{}/{}".format(user,toot))
    return response.json()
    
    
def follow(user,user_I_want_to_follow):
    response=requests.post("http://127.0.0.1:5000/start_following/{}/{}".format(user,user_I_want_to_follow))
    return response.json()
 
    
def unfollow(user,user_I_want_to_unfollow):
    response=requests.delete("http://127.0.0.1:5000/start_unfollowing/{}/{}".format(user,user_I_want_to_unfollow))
    return response.json()


def show_timeline(user):
    response=requests.get("http://127.0.0.1:5000/show_timeline/{}".format(user))
    return response.json()




