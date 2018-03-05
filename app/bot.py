import logging
import asyncio
import os.path
import random
import discord
from configobj import ConfigObj
from models import Participant

# 
# #initialize config file
# try:
#     config = ConfigObj('./files/botdata.cfg')
# except: 
#     os.mkdir('./files/')
#     config = ConfigObj('./files/botdata.cfg')
#     config['programData'] = {'exchange_started': False, 'discord_token': 'NDIwMjkyMzExODg1NTQ1NDg5.DX9Jkw._HbYEeQhcSC1P9AfUKWYuduLGGg'}
#     config['members'] = {}
#     config.write()

#initialize data from config file
usr_list = []
total_users = 0
exchange_started = config['programData'].as_bool('exchange_started')
for key in config['members']:
    total_users = total_users + 1
    usr_list.append(Participant(key[0], key[1], total_users, key[2], key[3], key[4]))

#initialize client class instance
client = discord.Client()

#handler for all on_message events
@client.event
async def on_message(message):
    #declare global vars
    
    #ignore messages from the bot itself
    if message.author == client.user:
        return
    
    #event for a user joining the secret santa
    elif message.content.startswith('$$addparticipant'):

        #Add participant instance by calling api --> POST
#         
#       await client.send_message(message.channel, message.author.mention + ' Has been added to the OfficialFam Secret Santa exchange!')
#       await client.send_message()
    
    elif message.content.startswith('$$getpartner'):
        #Call API to obtein parnet
    

@client.event
async def on_ready():
    """print message when client is connected"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#event loop and discord initiation
try:
    client.run(config['token'])
except discord.LoginFailure:
    print('Error: The token in /files/botdata.cfg is invalid')