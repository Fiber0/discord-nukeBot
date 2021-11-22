# CXC, Discord spam(nuke) bot

# Features
- can spam '@everyone' in selcted channel of a guild(server), affected by the message send limit

- can generate channels until 500(maximum) is reached

- can type '@everyone' in each channel generated, even after 500 is reached

- read 'cxc manual.txt' for more information

# Setup

copy content from cxc folder and save it in folder on your desktop

open CXC.py file in python editor(you can use replit.com)

change 'token' (at the end of the file) to your generated discord bot token, you can watch this video, if you're having trouble with this step:
https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org

you can then use https://uptimerobot.com to constantly ping the server, where is the bot hosted, better explanation in the video above(58:30- 1:03:36)

in OAuth2 in https://discord.com/developers (here select bot you previously made), select URL generator, tick 'bot', set permissions=45097290800 in
the URL at the bottom of the page

now copy the URL and search it, select server you want the bot to be and click 'Authorizate' !You must have 'manage server permission in order to Authorizate it!
