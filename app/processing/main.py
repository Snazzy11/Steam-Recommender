"""
File for running 'main code' and putting together pieces during development
"""
import os
import random

from dotenv import load_dotenv

from app.steam_connector import SteamApi
from app.data import user

load_dotenv()

# Create connector and User class
Connector = SteamApi(os.getenv('STEAM_API_KEY')) # Connector needs API key
User = user.User(os.getenv('MY_STEAM_ID')) # User needs a steam ID

# Init Steam class
Steam = SteamApi(os.getenv('STEAM_API_KEY'))

# Get response from steam api
games_response = Steam.get_owned_games(User.get_steam_id())
print('Games Response:', games_response)

# Transform into game objects
User.set_owned_games(games_response.get_owned_games())

print('A game: ', random.choice(User.owned_games))
