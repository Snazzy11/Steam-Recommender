"""
File for running 'main code' and putting together pieces during development
"""
import os
from dotenv import load_dotenv

from app.steam_connector import SteamApi
from app.data import user

load_dotenv()



Connector = SteamApi(os.getenv('STEAM_API_KEY'))
User = user.User(os.getenv('MY_STEAM_ID'))

Steam = SteamApi(os.getenv('STEAM_API_KEY'))
player_games = Steam.get_owned_games(User.get_steam_id())
print(player_games)
