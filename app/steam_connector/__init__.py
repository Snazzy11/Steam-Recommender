"""
Provides the connection to the Steam API
"""
# TODO: Use an interface or something so that when responses fail there is a fallback
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
    def __init__(self, json_data_string='', error=None):
        self.str_raw_json = json_data_string or ''
        self.error = error
        self.success = error is None and json_data_string != ''
        self.data = None
        self.pretty_json = ''

        if self.success:
            try:
                self.data = json.loads(json_data_string)
                self.pretty_json = json.dumps(self.data, indent=2)
            except json.JSONDecodeError as e:
                self.success = False
                self.error = f"JSON decode error: {e}"
                self.data = None


    def __str__(self):
        return self.pretty_json if self.success else f"<Error: {self.error}>"

class SteamApi:
    """
    Provides the connection to the Steam API. Also provides functions to fetch from the Steam API
    This class is NOT for processing data returned from the Steam API
    The functions will return Python objects which will have their own data and methods to process them
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_owned_games(self, player_id: str) -> ApiItem:
        """
        Queries the Steam API for games owned by a player
        :method: IPlayerService
        :param player_id: Numerical player ID
        :return: ApiItem object
        """
        url = (f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'
               f'?key={self.api_key}&steamid={player_id}&format=json')
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return ApiItem(error=str(e))
        return ApiItem(response.text)

    def get_game_stats(self, player_id: str, game_id: str,
                       date_range_start='2000-01-01', date_range_end='2030-01-01') -> ApiItem:
        """
        Queries the Steam API for game statistics for a plyaer on a specific game
        :method: ISteamGameServerStats
        :param player_id: Numerical player ID
        :param game_id: Numerical game or APP ID (has specific logic but should usually be unnecessary)
        :param date_range_start: Format YYYY-MM-DD HH:MM:SS the starting date to query
        :param date_range_end: Format YYYY-MM-DD HH:MM:SS the ending date to query
        :return: ApiItem object
        """
        url = (f'http://partner.steam-api.com/ISteamGameServerStats/GetGameServerPlayerStatsForGame/v1/'
               f'?key={player_id}&gameid={game_id}&appid={game_id}'
               f'&rangestart={date_range_start}&rangeend={date_range_end}')
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return ApiItem(error=str(e))
        return ApiItem(response.text)



SteamApi = SteamApi(os.getenv('STEAM_API_KEY'))

print(SteamApi.get_game_stats(os.getenv('MY_STEAM_ID'), '1172470'))
# print(SteamApi.player_get_owned_games(os.getenv('MY_STEAM_ID')).pretty_json)
