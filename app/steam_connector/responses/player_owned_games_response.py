"""
Holds the response class for the get_owned_games method
"""
from typing import List

from app.data.model.game_model import Game
from app.data.response_data.player_owned_games_data import PlayerOwnedGames
from app.steam_connector.responses.base_response import BaseResponse

# TODO: Allow/Disallow the 'include_appinfo' bool which will retrive additional data about each game
# TODO: Create an array of miniature 'game' objects


class PlayerGetOwnedGamesResponse(BaseResponse):
    """
    Response for the get_owned_games method
    Note that with default arguments, this API query does not make game names available
    """ # TODO: Denote that this is a 'simple' fetch
    owned_games: List[Game]


    def __init__(self, json_response: str, error=None) -> None:
        super().__init__(json_response, error)
        self._set_vars()


    # TODO: Only do if base response was successful
    def _set_vars(self) -> None:
        self.owned_games = []

        # TODO: How should I structure this? Is it okay to go over the field limit so I dont have to manage a playtime class and a game class?
        for game in self.data.response.games:
            self.owned_games.append(
                Game(
                    appid=game.appid,
                    name=game.name,
                    playtime=game.playtime_forever,
                    rtime_last_played=game.rtime_last_played,
                    playtime_windows=game.playtime_windows_forever,
                    playtime_linux=game.playtime_linux_forever,
                    playtime_mac=game.playtime_mac_forever,
                    playtime_deck=game.playtime_deck_forever,
                    playtime_disconnected=game.playtime_disconnected,
                    img_icon_url=game.img_icon_url
                )
            )

    def get_owned_games(self) -> List[Game]:
        """
        Get the list of owned games
        :return:
        """
        return self.owned_games

""" Response format
self
    data
        response
            game_count: int
            games: {
                000: ...
                001: {
                    appid: int
                    etc.
                }
            }
"""
