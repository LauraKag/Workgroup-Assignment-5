# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:54:45 2018

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



from flask import Flask, jsonify 

tooterserver = Flask("tooter server")

users={"Isabella": {
        "followers": [],
        "following":[],
        "toots":[]},
       "Candela":{
        "followers": [],
        "following":[],
        "toots":[]},
        "Yasmine":{
        "followers": [],
        "following":[],
        "toots":[]},
        "Laura":{
        "followers": [],
        "following":[],
        "toots":[]},
        "Eduardo":{
        "followers": [],
        "following":[],
        "toots":[]},
        "Arthur":{
        "followers": [],
        "following":[],
        "toots":[]},
        "Marius":{
        "followers": [],
        "following":[],
        "toots":[]}
        }

#• A user can create a toot
@tooterserver.route("/post_toot/<user>/<toot>",methods=["POST"])
def post_toot(user,toot):
    users[user]["toots"].append(toot)
    return jsonify(user + " toots: " + toot)



#• A user can delete a toot
@tooterserver.route("/delete_toot/<user>/<toot>",methods=["DELETE"])
def delete_toot(user,toot):
    users[user]["toots"].remove(toot)
    return jsonify("You just deleted the following toot: "+ toot)


#• A user can follow other users
@tooterserver.route("/start_following/<user>/<user_I_want_to_follow>",methods=["POST"])
def start_following(user,user_I_want_to_follow):
    if user_I_want_to_follow not in users[user]["following"] and user not in users[user_I_want_to_follow]["followers"]:
        users[user]["following"].append(user_I_want_to_follow)
        users[user_I_want_to_follow]["followers"].append(user)
        return jsonify("You are now a follower of: "+str(user_I_want_to_follow))


#• A user can unfollow other users
@tooterserver.route("/start_unfollowing/<user>/<user_I_want_to_unfollow>", methods=["DELETE"])
def start_to_unfollowing(user,user_I_want_to_unfollow):
    if user_I_want_to_unfollow in users[user]["following"] and user in users[user_I_want_to_unfollow]["followers"]:
        users[user]["following"].remove(user_I_want_to_unfollow)
        users[user_I_want_to_unfollow]["followers"].remove(user)
        return jsonify("You are not a follower of: "+str(user_I_want_to_unfollow)+ " anymore")


#• A user can see their timeline. Their timeline should contain all their
#own toots + all the toots of all the people they follow.
@tooterserver.route("/show_timeline/<user>")
def show_timeline(user):
    timeline={}
    timeline[user]=users[user]["toots"]
    for user in users[user]["following"]:
        timeline[user]=users[user]["toots"]
        
    return jsonify(timeline)
        

 
#Homepage should show the users-dictonary
@tooterserver.route("/homepage")
def homepage():
    return jsonify(users)


tooterserver.run()






