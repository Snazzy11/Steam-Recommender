"""
Provides the connection to the Steam API. Also provides functions to fetch from the Steam API
"""

import os
import json

from dotenv import load_dotenv

import requests

load_dotenv()
steam_api_key = os.getenv('STEAM_API_KEY')


class ApiItem:
    """
    A method provider for returned JSON data.
    """
    data = object
    str_raw_json = ''
    pretty_json = ''

    def __init__(self, json_data_string):
        self.str_raw_json = json_data_string
        self.data = json.loads(json_data_string)
        self.pretty_json = json.dumps(self.data, indent=2)

    def __str__(self):
        return self.str_raw_json


class SteamApi:
    """
    Provides the connection to the Steam API. Also provides functions to fetch from the Steam API
    This class is NOT for processing data returned from the Steam API
    The functions will return Python objects which will have their own data and methods to process them
    """

    url_GetOwnedGames = ('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + steam_api_key +
                         '&steamid=' + '%PLAYERID%' + '&format=json')

    def player_get_owned_games(self, player_id: str) -> json:
        """
        Queries the Steam API for games owned by a player
        :return: Full json text response from the Steam API
        """

        url = self.url_GetOwnedGames.replace('%PLAYERID%', player_id)

        response = requests.get(url, timeout=5)
        return ApiItem(response.text)



SteamApi = SteamApi()

# print(SteamApi.player_get_owned_games(os.getenv('MY_STEAM_ID')).pretty_json)
