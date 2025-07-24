"""
Provides the connection to the Steam API
"""
# TODO: Use an interface or something so that when responses fail there is a fallback
import os
import json
from dotenv import load_dotenv
import requests

from app.steam_connector.responses.base_response import BaseResponse
from app.steam_connector.responses.player_owned_games_response import PlayerGetOwnedGamesResponse

load_dotenv()
steam_api_key = os.getenv('STEAM_API_KEY')

class SteamApi:
    """
    Provides the connection to the Steam API. Also provides functions to fetch from the Steam API
    This class is NOT for processing data returned from the Steam API
    The functions will return response which will have their own data and methods to process them
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_owned_games(self, player_id: str | int) -> PlayerGetOwnedGamesResponse:
        """
        Queries the Steam API for games owned by a player
        :method: IPlayerService
        :param player_id: Numerical player ID
        :return: Response object
        """
        # TODO: If player id doesnt look like it correctly exists, throw an error
        url = (f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'
               f'?key={self.api_key}&steamid={str(player_id)}&format=json')
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return PlayerGetOwnedGamesResponse('', error=str(e))
        return PlayerGetOwnedGamesResponse(response.text)

    def get_game_stats(self, player_id: str | int, game_id: str | int,
                       date_range_start='2000-01-01', date_range_end='2030-01-01') -> BaseResponse:
        """
        Queries the Steam API for game statistics for a plyaer on a specific game
        :method: ISteamGameServerStats
        :param player_id: Numerical player ID
        :param game_id: Numerical game or APP ID (has specific logic but should usually be unnecessary)
        :param date_range_start: Format YYYY-MM-DD HH:MM:SS the starting date to query
        :param date_range_end: Format YYYY-MM-DD HH:MM:SS the ending date to query
        :return: Response object
        """
        url = (f'http://partner.steam-api.com/ISteamGameServerStats/GetGameServerPlayerStatsForGame/v1/'
               f'?key={str(player_id)}&gameid={str(game_id)}&appid={game_id}'
               f'&rangestart={date_range_start}&rangeend={date_range_end}')
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return BaseResponse(error=str(e))
        return BaseResponse(response.text)



# SteamApi = SteamApi(os.getenv('STEAM_API_KEY'))

# print(SteamApi.get_game_stats(os.getenv('MY_STEAM_ID'), '1172470'))
# print(SteamApi.player_get_owned_games(os.getenv('MY_STEAM_ID')).pretty_json)
